import re

UpperCaseLetters = re.compile("[A-Z]")

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

newRules = []
for r in rules:
    index = 0
    atomsRight = []
    while index<len(r[1]):
        if UpperCaseLetters.match(r[1][index]) and index<len(r[1])-1 and not UpperCaseLetters.match(r[1][index+1]):
          atomsRight.append(r[1][index:index+2])
          index += 1
        else:
          atomsRight.append(r[1][index:index+1])
        index += 1
    newRules.append([r[0], atomsRight])

#print newRules

index = 0
targetAtoms = []
while index<len(target):
  if UpperCaseLetters.match(target[index]) and index<len(target)-1 and not UpperCaseLetters.match(target[index+1]):
    targetAtoms.append(target[index:index+2])
    index += 1
  else:
    targetAtoms.append(target[index:index+1])
  index += 1

#print target
#print targetAtoms

def longMatch(string):
  result = 0
  while string[result] == targetAtoms[result] and result < len(string) and result < len(targetAtoms):
    result += 1
  return result

def backTrack(fromAtom, toAtom):
  rules = [r for r in newRules if r[1][0] == toAtom]
  #print fromAtom, toAtom, rules
  matches = [r for r in rules if r[0] == fromAtom]
  if len(matches) > 0:
    return [m + [1] for m in matches]
  else:
    results = []
    for r in rules:
      partials = backTrack(fromAtom, r[0])
      for p in partials:
        #print fromAtom, toAtom, r, p
        results.append([fromAtom, r[1] + p[1][1:], p[2]])
    return results


molecules = [(0,'e', 0)]
count = 0
while molecules[0][1] != target:
    molecule = molecules[0]
    molecules = molecules[1:]
    ln = longMatch(molecule[1])
    fromAtom = molecule[1][ln]
    toAtom = targetAtoms[ln]
    solutions = backTrack(fromAtom, toAtom)
    print ln, fromAtom, toAtom
    for s in solutions:
        print "", s
    print ""
    count += 1
    molecules = molecules + solutions

    if count > 1:
      break

#def process(value, rules):
#    results = set()
#    index = longMatch(value)
#    for (a,b) in rules:
#      strIndex = value.find(a, index)
#      if strIndex == index:
#          newStr = value[0:strIndex] + b + value[strIndex+len(a):]
#          results.add(newStr)
#    return list(results)
#
#print target
#print len(target)
#molecules = [(0,'e')]
#count = 0
#while molecules[0][1] != target:
#    molecule = molecules[0]
#    molecules = molecules[1:]
#    for newMolecule in process(molecule[1], rules):
#        molecules.append((molecule[0]+1,newMolecule))
#    molecules.sort(key=lambda x: - longMatch(x[1]) + x[0]/10)
#    if len(molecules) > 5000: molecules = molecules[0:2500]
#    count += 1
#    if count % 1000 == 0:
#      ln = longMatch(molecules[0][1])
#      print len(molecules), ln, molecules[0][0], molecules[0][1][0:ln] + " " + molecules[0][1][ln:]
#print molecules
