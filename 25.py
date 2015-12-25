start = 20151125
mult = 252533
rem = 33554393

row = 2981
col = 3075

def findIndex(row, col):
  both = row+col-1
  num = both*(both+1)/2 - (row-1)
  return num

print 4, 3, findIndex(4, 3)

num = findIndex(row, col)
print num

cnt = 1
while cnt < num:
  start = (start * mult) % rem
  cnt += 1
print start
