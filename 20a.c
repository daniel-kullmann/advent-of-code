#include <stdio.h>

long calculate(long input) {
  long factorSum = 1 + input;
  long i;
  for (i=2; i < input/2+1; i++) {
    if (input % i == 0 && input / i <= 50) {
      factorSum += i;
    }
  }
  return factorSum * 11;
}

int main() {
  long goal = 34000000;

  long solution = 831000;

  long result = calculate(solution);
  long maxResult = result;
  while (result < goal) {
    solution += 1;
    result = calculate(solution);
    maxResult  = result > maxResult ? result : maxResult;
    if (solution % 1000 == 0) {
      printf("%i %i %i\n", solution, result, maxResult);
    }
  }
  printf("%i %i\n", solution, result);
}

