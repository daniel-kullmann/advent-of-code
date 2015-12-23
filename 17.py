buckets = map(int, filter(lambda s: s!= "", map( lambda s: s.strip(), open('17.txt', 'r').read().split("\n"))))
numBuckets = len(buckets)
#buckets = [20, 15, 10, 5, 5]
target = 150

def calculate(target, buckets, listSoFar):
  #print ">", target, buckets
  if target < 0:
    #print "< 0 (too much)"
    return 0
  if target == 0:
    print "< 1", listSoFar
    return 1
  if len(buckets) == 0:
    #print "< 0 (no buckets left)"
    return 0
  bucket = buckets[0]
  buckets = buckets[1:]
  sum = 0
  sum += calculate(target, buckets, listSoFar)
  sum += calculate(target-bucket, buckets, listSoFar + [str(numBuckets-len(buckets)) + ":" + str(bucket)])
  return sum

print calculate(target, buckets, [])
