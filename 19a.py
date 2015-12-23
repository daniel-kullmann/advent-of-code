rules = []
input = None
fh = open('19.txt', 'r')
for line in fh.readlines():
    line = line.strip()
    parts = line.split(" => ")
    if len(parts) == 2:
      rules.append(parts)
    else:
      input = line

def process(input, rules):
    results = set()
    for (a,b) in rules:
      strIndex = input.find(a)
      while strIndex >= 0:
          newStr = input[0:strIndex] + b + input[strIndex+len(a):]
          results.add(newStr)
          strIndex = input.find(a, strIndex+1)
    return list(results)

molecules = [(0,'e')]
while molecules[0][1] != input:
    molecule = molecules[0]
    molecules = molecules[1:]
    for newMolecule in process(molecule[1], rules):
        molecules.append((molecule[0]+1,newMolecule))
    #print len(molecules), min(map(len,map(lambda x: x[1], molecules)))
print molecules[0]
