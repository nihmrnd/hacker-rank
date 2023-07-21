n = int(input())
ar = list(map(int, input().rstrip().split()))

def birthCakeCandles(ar):
  n = len(ar)
  max_value_array = ar[0]
  quantity_max_candles = 0
  
  for i in range(n):
    if ar[i] > max_value_array:
      max_value_array = ar[i]
  for x in range(n):
    if ar[x] == max_value_array:
      quantity_max_candles += 1
  return quantity_max_candles
    
result = birthCakeCandles(ar)
print(result)
    

#---------- ANOTHER WAY TO SOLVE: ----------------#
    #for i in range(1, len(ar)):
        #if ar[i] > max_value_array:
            #max_value_array = ar[i]
            #quantity_max_candles = 1
        #elif ar[i] == max_value_array:
            #quantity_max_candles += 1