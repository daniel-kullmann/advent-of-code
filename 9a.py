import re

regex = re.compile("^([^ ]+) to ([^ ]+) = ([0-9]+)")

class Piece:
  def __init__(self, fromCity, toCity, distance):
    self.cities = [fromCity, toCity]
    self.distance = distance
  def __repr__(self):
    return "(Piece " + " to ".join(self.cities) + " = " + str(self.distance) + ")"

cities = set()
pieces = []
fh = open('9.txt', 'r')
for line in fh.readlines():
  line = line.strip()
  m = regex.match(line)
  if m:
    pieces.append(Piece(m.group(1), m.group(2), int(m.group(3))))
    cities.add(m.group(1))
    cities.add(m.group(2))
  else:
    print("ERROR: " + line)

cities = sorted(list(cities))

#print "\n".join([str(city) for city in cities])
#print "\n".join([str(piece) for piece in pieces])

def calculateRoute(currentCity, visitedCities=[]):
  if currentCity in visitedCities:
    raise currentCity + " already visited"
  visitedCities = visitedCities + [currentCity]
  if len(visitedCities) == len(cities):
    return 0

  availablePieces = [piece for piece in pieces if currentCity in piece.cities]
  restDistance = -1
  for piece in availablePieces:
    otherCity = piece.cities[1] if piece.cities[0] == currentCity else piece.cities[0]
    if otherCity in visitedCities:
      continue
    restDistance = max(restDistance, piece.distance + calculateRoute(otherCity, visitedCities))
  return restDistance
    

maxDistance = -1
for startCity in cities:
  currentDistance = calculateRoute(startCity)
  print startCity + ": " + str(currentDistance)
  maxDistance = max(maxDistance, currentDistance)
 
print maxDistance

