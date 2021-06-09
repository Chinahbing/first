import json

# data = {}
# data['']

f = open("config.txt", "r", encoding="utf-8")
data = json.loads(f.read())
print(type(data))
print(data)