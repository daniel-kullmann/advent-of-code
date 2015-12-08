fh = open('2.txt', 'r')
ribbon = 0
for line in fh.readlines():
  sizes = map(int, line.strip().split('x'))
  volume = sizes[0]*sizes[1]*sizes[2]
  largestLength = max(sizes)
  ribbon += volume + 2*(sum(sizes) - largestLength)
print ribbon

