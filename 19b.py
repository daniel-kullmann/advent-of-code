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

fromTo = [[r[0], r[1][0], 1, r[1]] for r in newRules]
oldLen = -1
newLen = len(fromTo)
cnt = 0
while newLen != oldLen:
  additionals = []
  for f1 in fromTo:
    for f2 in fromTo:
      if f1[0] == f2[1]:
        print "=", f2, f1
        print [f2[0], f1[1], f2[2]+1, f1[3] + f2[3][1:]]
        additionals.append([f2[0], f1[1], f2[2]+1, f1[3] + f2[3][1:]])
      pass
  for a in additionals:
    if len([f for f in fromTo if f[0] == a[0] and f[1] == a[1] and ''.join(a[3]).startswith(''.join(f[3]))]) == 0:
      fromTo.append(a)
    else:
      print "rejected ", a
  oldLen = newLen
  newLen = len(fromTo)
  cnt += 1
  if cnt > 4:
    break

#print fromTo
#
#def longMatch(string):
#  result = 0
#  while string[result] == target[result] and result < len(string) and result < len(target):
#    result += 1
#  return result
#
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
