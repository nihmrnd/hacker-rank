n = int(input().strip())
arr = []

for x in range(n):
  arr.append(list(map(int, input().rstrip().split()))) 

def diagonalDifference(arr):
  left_to_right_sum = 0
  right_to_left_sum = 0
  for i in range(n):
    left_to_right_sum += arr[i][i]
    right_to_left_sum += arr[i][n - i  - 1]
  
  sum = left_to_right_sum - right_to_left_sum
  if sum < 0:
    return -sum
  else:
    return sum
  
result = diagonalDifference(arr)
print(result)
