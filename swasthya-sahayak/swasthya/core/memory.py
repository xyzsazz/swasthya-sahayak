import json, os
MEM_FILE = os.path.join(os.path.dirname(__file__), '..', 'data', 'processed', 'memory.json')

def save_memory(key, data):
    os.makedirs(os.path.dirname(MEM_FILE), exist_ok=True)
    mem = {}
    if os.path.exists(MEM_FILE):
        try:
            mem = json.load(open(MEM_FILE))
        except:
            mem = {}
    mem[key] = data
    json.dump(mem, open(MEM_FILE,'w'), indent=2)

def load_memory(key):
    if os.path.exists(MEM_FILE):
        mem = json.load(open(MEM_FILE))
        return mem.get(key)
    return None