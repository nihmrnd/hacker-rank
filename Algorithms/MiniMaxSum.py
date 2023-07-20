ar = list(map(int, input().rstrip().split()))

def miniMaxSum(ar):
  total_array_sum = 0
  min_value = ar[0]
  max_value = ar[0]
  
  for i in range(len(ar)):
    total_array_sum += ar[i]
    if ar[i] < min_value:
      min_value = ar[i]
    if ar[i] > max_value:
      max_value = ar[i]
  
  min_sum = total_array_sum - min_value
  max_sum = total_array_sum - max_value
  
  return max_sum, min_sum

result = miniMaxSum(ar)
print(*result)