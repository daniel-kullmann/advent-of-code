from collections import defaultdict
from re import compile

reindeer = dict()

regex = compile(r"^([^ ]+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.$")

fh = open('14.txt', 'r')
for line in fh.readlines():
  m = regex.match(line.strip())
  if m:
    reindeer[m.group(1)] = map(int, (m.group(2), m.group(3), m.group(4)))
  else:
    print "ERROR : " + line

#Test:
#reindeer = {"Comet" : [14,10,127], "Dancer": [16, 11, 162]}

class State:
  def __init__(self, data):
    self.distance = 0
    self.points = 0
    self.state = "Running"
    self.stateChange = data[1]
    self.speed = data[0]
    self.run = data[1]
    self.rest = data[2]

results = dict()
for name, data in reindeer.iteritems():
  results[name] = State(data)

sec = 0
while sec < 2503:
  sec += 1
  for name, data in reindeer.iteritems():
    state = results[name]
    if state.state == "Running":
      state.distance += state.speed

    if sec == state.stateChange:
      if state.state == "Running":
        state.state = "Resting"
        state.stateChange = sec + state.rest
      else:
        state.state = "Running"
        state.stateChange = sec + state.run

  maxValue = max([r.distance for r in results.values()])
  top = [r for r in results.keys() if results[r].distance == maxValue]
  for r in top:
    results[r].points += 1

print [r + " " + str(results[r].distance) for r in results]
print [r + " " + str(results[r].points) for r in results]

