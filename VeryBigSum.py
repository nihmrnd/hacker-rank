n = int(input())
ar = list(map(int, input().split()))

def aVeryBigSum(ar):
  sum = 0
  for i in range(len(ar)):
    sum += ar[i]
  return sum
  
result = aVeryBigSum(ar)
print(result)