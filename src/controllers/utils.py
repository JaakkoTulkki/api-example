import json

def convert_body_to_dict(data):
    if isinstance(data, bytes):
        data = data.decode("utf-8")
    if not isinstance(data, dict):
        data = json.loads(data)
    return data
