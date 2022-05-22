a = int(input('enter first number\n'))
b = int(input('enter second number\n'))
while a != 0 and b != 0:
    print('One   step')
    if a > b:
        a = a % b
    else:
        b = b % a
print(a + b)