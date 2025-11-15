import os
from swasthya.agents.inventory_agent import parse_inventory_csv, inventory_analysis

def test_inventory_analysis():
    path = os.path.join('data','raw','sample_inventory.csv')
    df = parse_inventory_csv(path)
    report = inventory_analysis(df, lookahead_days=30)
    assert 'medicine' in report.columns
    assert report.shape[0] >= 1