"""Simple script to demo routing locally (not a production web server)."""
from swasthya.agents.router import create_session, route_input
import json, os, pandas as pd

if __name__ == '__main__':
    session = create_session('demo1', meta={'clinic':'Demo Clinic'})
    sample_case = {'age':8,'gender':'female','complaint':'Fever and headache since morning, one vomiting episode.'}
    print('Running symptom triage...')
    out = route_input('demo1','symptom', sample_case)
    print(json.dumps(out, indent=2))
    print('\nRunning inventory check...')
    inv_path = os.path.join('data','raw','sample_inventory.csv')
    inv_out = route_input('demo1','inventory', {'path':inv_path})
    print(inv_out['report_table'].head().to_string())