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

run = 2503
#Test:
#run = 1000
#reindeer = {"Comet" : [14,10,127], "Dancer": [16, 11, 162]}

stats = defaultdict(lambda: defaultdict(int))
results = dict()

for name, data in reindeer.iteritems():
  print name, data
  sec = 0
  distance = 0
  while sec < run:
    flySec = 0
    while flySec < data[1] and sec < run:
      distance += data[0]
      flySec += 1
      sec += 1
      stats[sec][name] = distance
    restSec = 0
    while restSec < data[2] and sec < run:
      restSec += 1
      sec += 1
      stats[sec][name] = distance
  results[name] = distance

for sec in stats.keys():
  data = stats[sec]
  maxValue = max(data.values())
  top = [r for r in data.keys() if data[r] == maxValue]
  for r in top:
    results[r] += 1

print results
