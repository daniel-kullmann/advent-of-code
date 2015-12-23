goal = 34000000

solution = 786240 - 20

def calculate(input):
  factorSum = 1 + input
  for i in range(2, input/2+1):
    if input % i == 0:
      factorSum += i
  return factorSum * 10

result = calculate(solution)
while result < goal:
  print solution, result
  solution += 1
  result = calculate(solution)

print solution, result
