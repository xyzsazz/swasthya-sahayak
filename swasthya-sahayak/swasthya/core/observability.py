import logging, json, time
logger = logging.getLogger('swasthya')
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)

def log_event(agent, input_type, outcome, duration_ms=None, extra=None):
    entry = {
        'agent': agent,
        'input_type': input_type,
        'outcome': outcome,
        'duration_ms': duration_ms,
        'extra': extra
    }
    logger.info(json.dumps(entry))