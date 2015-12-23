sue = {
  "children": 3,
  "cats": 7,
  "samoyeds": 2,
  "pomeranians": 3,
  "akitas": 0,
  "vizslas": 0,
  "goldfish": 5,
  "trees": 3,
  "cars": 2,
  "perfumes": 1
}

def matches(sue, aunt):
  for key in aunt.keys():
    if sue[key] != aunt[key]:
      return False
  return True

aunts = []
fh = open('16.txt', 'r')
for line in fh.readlines():
  parts1 = line.strip().split(":", 1)
  (_, number) = parts1[0].split(" ")
  parts2 = map(lambda s: s.strip(), parts1[1].split(", "))
  aunt = {el.split(": ")[0]: int(el.split(": ")[1]) for el in parts2}
  if matches(sue, aunt):
    print number

