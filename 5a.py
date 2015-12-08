import re

nice1 = re.compile("(..).*\\1")
nice2 = re.compile("(.).\\1")

fh = open('5.txt', 'r')
nice = 0
for line in fh.readlines():
  line = line.strip()
  if nice1.search(line) and nice2.search(line):
    nice += 1

print(nice)


