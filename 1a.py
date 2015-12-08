fh = open('1.txt')
content = fh.read()

floor = 0
pos = 1
for c in content:
  if c == '(': floor += 1
  elif c == ')': floor -= 1
  if floor < 0:
    print pos
    break
  pos += 1

