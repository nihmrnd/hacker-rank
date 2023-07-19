n = int(input())

def staircase(n):
  i = 1 
  while i < (n + 1):
    print(' ' * (n - i) + '#' * i)
    i += 1
  return exit()

result = staircase(n)
print(result)