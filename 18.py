SIZE=100
def makeGrid():
    return [ [0 for i in range(0,SIZE)] for j in range(0,SIZE)]

start = []

fh = open('18.txt', 'r')
for line in fh.readlines():
    start.append([c == '#' for c in line.strip()])

def calculateNext(grid):
    result = makeGrid()
    for y in range(0,SIZE):
      row = grid[y] 
      for x in range(0,SIZE):
        value = row[x]
        if value:
          if y > 0:
            if x > 0:
              result[y-1][x-1] += 1
            result[y-1][x] += 1
            if x < SIZE-1: 
              result[y-1][x+1] += 1

          if x > 0:
            result[y][x-1] += 1
          if x < SIZE-1: 
            result[y][x+1] += 1

          if y < SIZE-1:
            if x > 0:
              result[y+1][x-1] += 1
            result[y+1][x] += 1
            if x < SIZE-1: 
              result[y+1][x+1] += 1

    #print ""
    #for row in result:
    #    print row

    nextGrid = makeGrid()
    for y in range(0,SIZE):
      row = grid[y] 
      for x in range(0,SIZE):
        value = row[x]
        neighbors = result[y][x]
        nextGrid[y][x] = False
        if value and (neighbors == 2 or neighbors ==3):
            nextGrid[y][x] = True
        if not value and (neighbors ==3):
            nextGrid[y][x] = True

    return nextGrid

for iteration in range(0,SIZE):
    start = calculateNext(start)

print sum([sum ([ 1 if elem else 0 for elem in row]) for row in start])

#SIZE=6
#grid=[
#  [False, True , False, True , False, True],
#  [False, False, False, True , True , False],
#  [True , False, False, False, False, True],
#  [False, False, True , False, False, False],
#  [True , False, True , False, False, True],
#  [True , True , True , True , False, False]
#]
#
#print ""
#for row in grid:
#    print row
#grid = calculateNext(grid)
#print ""
#for row in grid:
#    print row

