import md5

s = "bgvyzdsv"
h = ""
i=0
while not h.startswith("000000"):
  m = md5.new()
  m.update(s+str(i))
  h = m.hexdigest()
  i += 1

print(i-1, h)

