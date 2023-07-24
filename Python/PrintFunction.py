n = int(input())
numbers = []

for i in range(1, n+1):
  numbers.append(i)

output_without_spaces = ''
for num in numbers:
  output_without_spaces += str(num)

print(output_without_spaces)

