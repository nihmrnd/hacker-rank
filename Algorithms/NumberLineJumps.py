first_multiple_input = input().rstrip().split()
x1 = int(first_multiple_input[0])
v1 = int(first_multiple_input[1])
x2 = int(first_multiple_input[2])
v2 = int(first_multiple_input[3])

def kangaroo(x1, v1, x2, v2):
  meet_at_the_same_time = None
  
  if v1 == v2:
    if x1 == x2:
      meet_at_the_same_time = 'YES'
    else:
      meet_at_the_same_time = 'NO'
  elif (x2 - x1) % (v1 - v2) == 0 and (v1 - v2) and (x2 - x1) // (v1 - v2) >= 0:
    meet_at_the_same_time = 'YES'
  else:
    meet_at_the_same_time = 'NO'
  return meet_at_the_same_time

result = kangaroo(x1, v1, x2, v2)
print(result)