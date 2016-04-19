import json

with open('op.json') as f:
    text_data = f.read()
data = json.loads(text_data)
