def process(value):
  result = ""
  current = None
  count = 0
  for char in value:
    if current == None:
      current = char
      count = 1
    elif current == char:
      count += 1
    else:
      result += str(count) + current
      current = char
      count = 1
  if count > 0:
    result += str(count) + current
  return result

value="3113322113"
for i in range(0,50):
  value=process(value)
print len(value)
