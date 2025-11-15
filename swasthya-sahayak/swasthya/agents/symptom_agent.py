import json, jsonschema
from swasthya.tools.mock_llm import MockLLM
from pprint import pprint

triage_schema = {
    "type":"object",
    "properties":{
        "severity":{"type":"string"},
        "recommended_action":{"type":"string"},
        "confidence":{"type":"number"},
        "followup_questions":{"type":"array"}
    },
    "required":["severity","recommended_action","confidence","followup_questions"]
}

def build_symptom_prompt(case):
    prompt = f"""You are a non-diagnostic medical triage assistant. Output MUST be valid JSON with keys: severity (low/medium/high), recommended_action (string), confidence (0-1 float), followup_questions (array of strings).

Patient details:
- Age: {case.get('age')}
- Gender: {case.get('gender')}
- Complaint: {case.get('complaint')}

Return JSON only."""
    return prompt

def run_symptom_agent(case, llm=None):
    llm = llm or MockLLM()
    prompt = build_symptom_prompt(case)
    response = llm.generate(prompt)
    parsed = json.loads(response['content'])
    try:
        jsonschema.validate(parsed, triage_schema)
    except Exception as e:
        parsed = {'error':'invalid_response','raw':response['content'],'exception':str(e)}
    return parsed

if __name__ == '__main__':
    case = {'age':45,'gender':'male','complaint':'Red swollen wound on left leg after falling 3 days ago.'}
    out = run_symptom_agent(case)
    pprint(out)