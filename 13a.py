from collections import defaultdict
from itertools import permutations
from re import compile

names = set()
points = defaultdict(lambda: defaultdict(int)) 
regex = compile(r"^([^ ]+) would (lose|gain) ([0-9]+) happiness units by sitting next to ([^ ]+).$")

fh = open('13.txt', 'r')
for line in fh.readlines():
  m = regex.match(line.strip())
  if m:
    names.add(m.group(1))
    names.add(m.group(4))
    value = int(m.group(3)) 
    if m.group(2) == "lose":
      value = - value
    points[m.group(1)][m.group(4)] += value
  else:
    print "ERROR : " + line

names = list(names) + ["Daniel"]

namePermutations = [p for p in permutations(names) if p[0] == names[0]]

def evaluate(names):
  result = 0
  numberOfNames = len(names)
  for i in range(0, numberOfNames):
    name = names[i]
    leftNeighbor = names[(i-1) % numberOfNames]
    rightNeighbor = names[(i+1) % numberOfNames]
    result += points[name][leftNeighbor]
    result += points[name][rightNeighbor]
  return result

print max([evaluate(p) for p in namePermutations])

