import pandas as pd, math, json
from swasthya.tools.mock_llm import MockLLM

def parse_inventory_csv(path):
    df = pd.read_csv(path, parse_dates=['expiry_date'])
    return df

def inventory_analysis(df, lookahead_days=30):
    today = pd.Timestamp('today').normalize()
    results = []
    for _, row in df.iterrows():
        med = row['medicine_name']
        qty = float(row['quantity'])
        daily_avg = float(row['daily_avg_usage']) if row['daily_avg_usage']>0 else 0.1
        days_until_stockout = qty / daily_avg if daily_avg>0 else float('inf')
        expiry_days = (pd.to_datetime(row['expiry_date']) - today).days
        need_in_30 = max(0, math.ceil((daily_avg * lookahead_days) - qty))
        priority = 'low'
        if need_in_30 > 0 and expiry_days > 30:
            priority = 'high'
        elif expiry_days <= 90:
            priority = 'medium'
        results.append({
            'medicine': med,
            'quantity': qty,
            'daily_avg': daily_avg,
            'days_until_stockout': round(days_until_stockout,1) if math.isfinite(days_until_stockout) else None,
            'expiry_in_days': expiry_days,
            'need_in_30': int(need_in_30),
            'priority': priority
        })
    return pd.DataFrame(results)

def run_inventory_agent(path, llm=None):
    llm = llm or MockLLM()
    df = parse_inventory_csv(path)
    report = inventory_analysis(df, lookahead_days=30)
    prompt = 'Inventory summary and recommendations'
    resp = llm.generate(prompt)
    return {'report_table': report, 'llm_summary': json.loads(resp['content'])}

if __name__ == '__main__':
    out = run_inventory_agent('data/raw/sample_inventory.csv')
    print(out['llm_summary'])
    print(out['report_table'].head())