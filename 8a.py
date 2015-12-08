fh = open('8.txt', 'r')
codeLength = 0
encodedStringLength = 0
for line in fh.readlines():
  line = line.strip()
  codeLength += len(line)
  if not line.startswith('"') or not line.endswith('"'):
    print "ERROR: " + line
    continue
  encodedStringLength += 2
  i = 0
  while i<len(line):
    if line[i] == '\\' or line[i] == '"':
      encodedStringLength += 2
    else:
      encodedStringLength += 1
    i += 1


print codeLength, encodedStringLength, encodedStringLength-codeLength

