import json

def formato_json(segmentacion):
    return (json.dumps(segmentacion, indent=2))