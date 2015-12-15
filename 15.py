import re

s = re.compile(r"([^:]+): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)")

ingredients = []
fh = open('15.txt', 'r')
for line in fh.readlines():
  m = s.match(line.strip())
  if m:
    ingredients.append((m.group(1), map(int, [m.group(2), m.group(3), m.group(4), m.group(5), m.group(6)])))
  else:
    print "ERROR: line"

def process(i1,i2,i3,i4):
  result = 1 
  for d in range(0,4):
    sum = ingredients[0][1][d] * i1 + ingredients[1][1][d] * i2 + ingredients[2][1][d] * i3 + ingredients[3][1][d] * i4
    if sum < 0:
      sum = 0
    result = result * sum
  return result 

result = -1
for i1 in range(0,101):
  for i2 in range(0,101):
    for i3 in range(0,101):
      result = max(result, process(i1,i2,i3,100-i1-i2-i3))

print result
