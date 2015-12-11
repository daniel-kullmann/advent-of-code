import string
import re

input = "cqjxjnds"

doublePairs = re.compile(r"^.*(.)\1.*(.)\2")

allLetters = "abcdefghijklmnopqrstuvwxyz"
allowedLetters = "abcdefghjkmnpqrstuvwxyz"

def incPassword(input):
  result = ""
  inc = 1
  for i in range(len(input)-1, -1, -1):
    char = input[i]
    charIndex = string.find(allowedLetters, char)
    if charIndex < 0:
      print "ERROR: " + input + " " + char
    elif charIndex+inc >= len(allowedLetters):
      char = allowedLetters[0]
      inc = 1
    elif inc > 0:
      char = allowedLetters[charIndex+inc]
      inc = 0
    else:
      char = char
      inc = 0
    result = char + result
  return result

def check(input):
  foundStraight = False
  for startIndex in range(0, len(allLetters)-2):
    toFind = allLetters[startIndex:startIndex+3]
    if string.find(input, toFind) >= 0:
      foundStraight = True
      break
  if not foundStraight:
    return False
  if not doublePairs.match(input):
    return False
  return True

print input
count = 0
while True:
  input = incPassword(input)
  if check(input):
    print
    print input, count
    break
  count += 1

