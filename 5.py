import re

nice1 = re.compile("^.*[aeiou].*[aeiou].*[aeiou]")
nice2 = re.compile("(.)\\1")
bad = re.compile("ab|cd|pq|xy")

fh = open('5.txt', 'r')
nice = 0
for line in fh.readlines():
  line = line.strip()
  if not bad.search(line):
    if nice1.search(line) and nice2.search(line):
      nice += 1

print(nice)


