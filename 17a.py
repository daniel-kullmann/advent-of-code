buckets = map(int, filter(lambda s: s!= "", map( lambda s: s.strip(), open('17.txt', 'r').read().split("\n"))))
numBuckets = len(buckets)
target = 150

def calculate(target, buckets, result, results):
  if target < 0:
    return
  if target == 0:
    results.append(result)
    return 
  if len(buckets) == 0:
    return 
  calculate(target, buckets[1:], result, results)
  calculate(target-buckets[0], buckets[1:], result + [str(numBuckets-len(buckets)) + ":" + str(bucket)], results)

results = []
calculate(target, buckets, [], results)
minNumber = min(map(len, results))
minNumberResults = filter(lambda item: len(item) == minNumber, results)
for item in minNumberResults:
  print item
print len(minNumberResults)

