import re

pairOfPairs = re.compile("(turn on|turn off|toggle) ([0-9]+),([0-9]+) through ([0-9]+),([0-9]+)")
lights = [[0 for i in range(0,1000)] for j in range(0,1000)]

fh = open('6.txt', 'r')
for line in fh.readlines():
  line = line.strip()
  m = pairOfPairs.match(line)
  if not m:
    print("ERROR " + line)
    continue
  (x1,y1,x2,y2) = (int(m.group(2)), int(m.group(3)), int(m.group(4)), int(m.group(5)))
  for x in range(x1,x2+1):
    for y in range(y1,y2+1):
      if m.group(1) == "turn on":
        lights[x][y] += 1
      elif m.group(1) == "turn off":
        if lights[x][y] > 0:
          lights[x][y] -= 1
      elif m.group(1) == "toggle":
        lights[x][y] += 2
      else:
        print("ERROR " + line)

nums = sum(map(sum, lights))
print(nums)


