from collections import defaultdict

fh = open('3.txt')
content = fh.read()

counter = defaultdict(int)

x=0
y=0
counter[str(x)+":"+str(y)] += 1
for c in content:
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

count = 0
for c in counter.values():
    if c >= 1:
        count += 1

print count
  
