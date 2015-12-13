import json
fh = open('12.txt', 'r')
data = json.loads(fh.read())

def process(data):
  sum = 0
  if type(data) is list:
    for item in data:
      sum += process(item)
  elif type(data) is dict:
    if not "red" in data.values():
      for item in data.values():
        sum += process(item)
  elif type(data) is int:
    sum += data
  elif type(data) is float:
    sum += data
  return sum

print process(data)

