import itertools
from operator import mul

packages = map(int, filter(lambda s: s!= "", map( lambda s: s.strip(), open('24.txt', 'r').read().split("\n"))))
oneSize = sum(packages) / 4

packages.sort()
packages.reverse()
minPackagesNeeded = 0
sizeForThis = 0
for p in packages:
    minPackagesNeeded += 1
    sizeForThis += p
    if sizeForThis >= oneSize:
        break

print oneSize, minPackagesNeeded


solution = None
solutionQe = None

def qe(values):
    return reduce(mul, values)

#packages.reverse()

for firstSize in range(minPackagesNeeded, len(packages)-minPackagesNeeded+1):
    for firstBatch in itertools.combinations(packages, firstSize):
        if sum(firstBatch) != oneSize:
            continue
        restPackages = list(set(packages) - set(firstBatch))
        for secondSize in range(max(firstSize, minPackagesNeeded), len(restPackages)-minPackagesNeeded+1):
            for secondBatch in itertools.combinations(restPackages, secondSize):
                if sum(secondBatch) != oneSize:
                    continue
                if len(secondBatch) < len(firstBatch):
                    continue
                if len(restPackages) - len(secondBatch) < len(firstBatch):
                    continue
        
                thisIsAPossibleSolution = False

                restPackages2 = list(set(restPackages) - set(secondBatch))
                for thirdSize in range(max(firstSize, minPackagesNeeded), len(restPackages2)-minPackagesNeeded+1):
                    for thirdBatch in itertools.combinations(restPackages2, thirdSize):

                        #solution found
                        thisIsAPossibleSolution = True
                        if solution == None:
                            solution = len(firstBatch)
                            solutionQe = qe(firstBatch)
                            print solution, solutionQe, firstBatch, secondBatch, thirdBatch
                        elif len(firstBatch) < solution:
                            solution = len(firstBatch)
                            solutionQe = qe(firstBatch)
                            print solution, solutionQe, firstBatch, secondBatch, thirdBatch
                        elif len(firstBatch) == solution:
                            if qe(firstBatch) < solutionQe:
                                solutionQe = qe(firstBatch)
                                print solution, solutionQe, firstBatch, secondBatch, thirdBatch
                            else:
                                print "", solution, solutionQe, firstBatch, secondBatch, thirdBatch
                        else:
                            print "", solution, solutionQe, firstBatch, secondBatch, thirdBatch
                        # thisIsAPossibleSolution
                        break
                if thisIsAPossibleSolution:
                    break
    if solution != None:
        # All other solutions will be larger
        break

print solution
print solutionQe
