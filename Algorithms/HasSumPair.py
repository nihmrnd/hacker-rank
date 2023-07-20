"""
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given[10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
"""


def has_sum_pair(numbers, k):
    # Check all pairs of numbers for a sum equal to k
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == k:
                return (numbers[i], numbers[j])

    # No pair of numbers adds up to k
    return False


numbers = []
while True:
    val = int(input("Enter an array element (-1 to stop): "))
    if val == -1:
        break
    numbers.append(val)
k = int(input('Enter a value for k:'))
result = has_sum_pair(numbers, k)


print(f"The input list is {numbers}, and k is {k}. The result is {result}.")