fh = open('2.txt', 'r')
area = 0
for line in fh.readlines():
  sizes = map(int, line.strip().split('x'))
  sides = [sizes[0]*sizes[1], sizes[1]*sizes[2], sizes[0]*sizes[2]]
  smallestSide = min(sides)
  area += smallestSide + 2*sum(sides)
print area

