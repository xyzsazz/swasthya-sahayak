from swasthya.agents.symptom_agent import run_symptom_agent
from swasthya.agents.image_agent import run_image_agent
from swasthya.agents.inventory_agent import run_inventory_agent

SESSIONS = {}

def create_session(session_id, meta=None):
    SESSIONS[session_id] = {'history':[], 'meta': meta or {}}
    return SESSIONS[session_id]

def route_input(session_id, input_type, payload):
    sess = SESSIONS.get(session_id) or create_session(session_id)
    sess['history'].append({'type':input_type, 'payload':payload})
    if input_type == 'symptom':
        out = run_symptom_agent(payload)
        sess['last_triage'] = out
        return out
    if input_type == 'image':
        out = run_image_agent(payload.get('bytes', b''), payload.get('meta', {}))
        sess['last_image'] = out
        return out
    if input_type == 'inventory':
        out = run_inventory_agent(payload.get('path'))
        sess['last_inventory'] = out
        return out
    return {'error':'unknown_input_type'}