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

def process(target, rules):
    results = set()
    for (a,b) in rules:
      strIndex = target.find(a)
      while strIndex >= 0:
          newStr = target[0:strIndex] + b + target[strIndex+len(a):]
          results.add(newStr)
          strIndex = target.find(a, strIndex+1)
    return list(results)

def longMatch(string):
  result = 0
  while string[result] == target[result] and result < len(string) and result < len(target):
    result += 1
  return result

print len(target)
molecules = [(0,'e')]
count = 0
while molecules[0][1] != target:
    molecule = molecules[0]
    molecules = molecules[1:]
    for newMolecule in process(molecule[1], rules):
        molecules.append((molecule[0]+1,newMolecule))
    molecules.sort(key=lambda x: x[0] - longMatch(x[1]))
    if len(molecules) > 5000: molecules = molecules[0:2500]
    count += 1
    if count %100 == 0:
      print len(molecules), longMatch(molecules[0][1]), molecules[0]
print molecules[0]
