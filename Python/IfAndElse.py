n = int(input())

if n <=5 and n % 2 == 0 :
    print('Not Weird')
elif n <=20 and n % 2 == 0:
    print('Weird')
elif n > 20 and n % 2 == 0:
    print('Not Weird')
else:
    print('Weird')