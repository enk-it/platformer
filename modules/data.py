import json

with open('data/settings.json', 'r') as f:
    text_data = f.read()
    settings = json.loads(text_data)


with open('data/player_data.json', 'r') as f:
    text_data = f.read()
    player_data = json.loads(text_data)


with open('data/cached_level.json', 'r') as f:
    text_data = f.read()
    cached_level = json.loads(text_data)