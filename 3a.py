from collections import defaultdict

fh = open('3.txt')
content = fh.read()

counter = defaultdict(int)

x=0
y=0
rx=0
ry=0
robo=True
counter[str(x)+":"+str(y)] += 1
for c in content:
    if robo:
      if c == '^':
        ry -= 1
      elif c == 'v':
        ry += 1
      elif c =='<':
        rx -= 1
      elif c == '>':
        rx += 1
      else:
        print "Unknown char: " + c
      counter[str(rx)+":"+str(ry)] += 1
    else:
      if c == '^':
        y -= 1
      elif c == 'v':
        y += 1
      elif c =='<':
        x -= 1
      elif c == '>':
        x += 1
      else:
        print "Unknown char: " + c
      counter[str(x)+":"+str(y)] += 1
    robo = not robo


count = 0
for c in counter.values():
    if c >= 1:
        count += 1

print count
  
