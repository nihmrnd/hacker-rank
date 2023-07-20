array_size = int(input())
ar = []
ar = list(map(int, input().split()))

def simpleArraySum(ar):
  sum = 0
  for x in range(len(ar)):
    sum = sum + ar[x]
  return sum 

result = simpleArraySum(ar)
print(result)
exit()

