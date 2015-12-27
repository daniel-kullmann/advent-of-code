rules = []
target = None
fh = open('19.txt', 'r')
for line in fh.readlines():
    line = line.strip()
    parts = line.split(" => ")
    if len(parts) == 2:
      rules.append(parts)
    else:
      target = line

def longMatch(string):
  result = 0
  while string[result] == target[result] and result < len(string) and result < len(target):
    result += 1
  return result

def process(value, rules):
    results = set()
    index = longMatch(value)
    for (a,b) in rules:
      strIndex = value.find(a, index)
      if strIndex == index:
          newStr = value[0:strIndex] + b + value[strIndex+len(a):]
          results.add(newStr)
    return list(results)

print target
print len(target)
molecules = [(0,'e')]
count = 0
while molecules[0][1] != target:
    molecule = molecules[0]
    molecules = molecules[1:]
    for newMolecule in process(molecule[1], rules):
        molecules.append((molecule[0]+1,newMolecule))
    molecules.sort(key=lambda x: - longMatch(x[1]) + x[0]/10)
    if len(molecules) > 5000: molecules = molecules[0:2500]
    count += 1
    if count % 1000 == 0:
      ln = longMatch(molecules[0][1])
      print len(molecules), ln, molecules[0][0], molecules[0][1][0:ln] + " " + molecules[0][1][ln:]
print molecules
