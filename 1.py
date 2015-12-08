
fh = open('1.txt')
content = fh.read()

counter = {
  '(': 0,
  ')': 0,
}
for c in content:
  counter[c] += 1

print counter['(']-counter[')']
