total_array_quantity = int(input().strip())
ar = list(map(int, input().split()))

def plusMinus(ar):
  positive = 0
  negative = 0
  zero = 0
  for i in ar:
    if i > 0:
      positive += 1
    elif i < 0:
      negative += 1
    else:
      zero += 1
  
  positive_ratio = positive / total_array_quantity
  negative_ratio = negative / total_array_quantity
  zero_ratio = zero / total_array_quantity
  
  return positive_ratio,negative_ratio,zero_ratio

result = plusMinus(ar)
for ratio in result:
    print("{:.6f}".format(ratio))