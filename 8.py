fh = open('8.txt', 'r')
codeLength = 0
stringLength = 0
for line in fh.readlines():
  line = line.strip()
  codeLength += len(line)
  if not line.startswith('"') or not line.endswith('"'):
    print "ERROR: " + line
    continue
  i = 1
  while i<len(line)-1:
    if line[i] == '\\':
      if line[i+1] == 'x':
        i += 4
      else:
        i += 2
    else:
      i += 1
    stringLength += 1

print codeLength, stringLength, codeLength-stringLength

