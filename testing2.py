import json

with open('data/newrepublic.json', 'r') as f:
  data = json.load(f)

print(data[0]["title"])