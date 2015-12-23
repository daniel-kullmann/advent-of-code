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
    return len(results)

print len(rules)
print process(input, rules)
