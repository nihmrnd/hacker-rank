a = list(map(int, input().strip().split()))
b = list(map(int, input().strip().split()))

def compareTriplets(a,b):
  
  alice = 0
  bob = 0
  
  for i in range(len(a)):
        if a[i] == b[i]:
          continue
        elif a[i] > b[i]:
          alice += 1
        else: 
          bob += 1
  return [alice,bob]

result = compareTriplets(a,b)
print(*result)
