import json
from swasthya.tools.mock_llm import MockLLM

def run_image_agent(image_bytes, metadata, llm=None):
    llm = llm or MockLLM()
    desc = metadata.get('desc','')
    prompt = f"Image findings: {desc} -- provide severity and recommended_action in JSON."
    resp = llm.generate(prompt)
    parsed = json.loads(resp['content'])
    mapping = {'low':0.2,'medium':0.5,'medium-high':0.75,'high':0.95}
    score = mapping.get(parsed.get('severity','medium'),0.5)
    return {'severity_score':score,'visual_findings':[parsed.get('recommended_action')],'next_steps':parsed.get('recommended_action')}

if __name__ == '__main__':
    out = run_image_agent(b'binary', {'desc':'swollen wound on leg with redness'})
    print(out)