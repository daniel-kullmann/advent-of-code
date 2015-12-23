goal = 34000000

solution = 786240

def calculate(input):
  factorSum = 1 + input
  for i in range(2, input/2+1):
    if input % i == 0 and input / i <= 50:
      factorSum += i
  return factorSum * 11

result = calculate(solution)
maxResult = result
while result < goal:
  solution += 1
  result = calculate(solution)
  maxResult  = max(result, maxResult)
  if solution % 1000 == 0:
    print solution, result, maxResult

