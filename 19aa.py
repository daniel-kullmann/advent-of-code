import sha
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

def key(string):
  return sha.new(string).hexdigest()

print target
print len(target)
seen = set()
molecules = [(0,target)]
count = 0
tries = 0
misses = 0
while len(molecules) > 0: #molecules[0][1] != 'e':
    molecule = molecules[0]
    molecules = molecules[1:]
    newMolecules = []
    for r in rules:
        index = molecule[1].rfind(r[1])
        if index >= 0:
            newMolecule = molecule[1][0:index] + r[0] + molecule[1][index+len(r[1]):]
            if not key(newMolecule) in seen:
                newMolecules.append((molecule[0]+1,newMolecule))
                seen.add(key(newMolecule)
        else:
            misses += 1
        tries += 1
    for m in newMolecules:
      molecules.append(m)
    molecules.sort(key=lambda x: + len(x[1]))
    count += 1
    if count % 100 == 0:
      print tries, misses, len(molecules), len(molecules[0][1]), molecules[0][0], molecules[0][1]
print molecules[0]
