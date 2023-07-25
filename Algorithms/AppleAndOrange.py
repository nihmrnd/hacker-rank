first_multiple_input = input().rstrip().split()
s = int(first_multiple_input[0])
t = int(first_multiple_input[1])

second_multiple_input = input().rstrip().split()
a = int(second_multiple_input[0])
b = int(second_multiple_input[1])

third_multiple_input = input().rstrip().split()
m = int(third_multiple_input[0])
n = int(third_multiple_input[1])

apples = list(map(int, input().rstrip().split()))
oranges = list(map(int, input().rstrip().split()))

def countApplesAndOranges(s, t, a, b, apples, oranges):
  
  result_apple_operations = []
  result_orange_operations = []
  
  for x in apples:
    if x < 0:
      negative_count_apple = a - abs(x)
      result_apple_operations.append(negative_count_apple)
    else:
      positive_count_apple = a + abs(x)
      result_apple_operations.append(positive_count_apple)

  for i in oranges:
    if i < 0:
      negative_count_orange = b - abs(i)
      result_orange_operations.append(negative_count_orange)
    else:
      positive_count_orange = b + abs(i)
      result_orange_operations.append(positive_count_orange)

  apple_in_sam_house = 0
  orange_in_sam_house = 0
  for apple in result_apple_operations:
    if s <= apple <= t:
      apple_in_sam_house += 1
  
  for orange in result_orange_operations:  
    if s <= orange <= t:
      orange_in_sam_house += 1
  
  return apple_in_sam_house, orange_in_sam_house
            
result = countApplesAndOranges(s, t, a, b, apples, oranges)
apple_result, orange_result = result
print(apple_result)
print(orange_result)