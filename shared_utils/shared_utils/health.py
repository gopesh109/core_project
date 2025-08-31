import datetime

def get_health():
    return {
        'status': 'ok',
        'timestamp': datetime.datetime.utcnow().isoformat()
    }
