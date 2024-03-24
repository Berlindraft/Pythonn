#calculator in python

num1 = int(input('enter a number:  '))
num2 = int(input('enter another number:  '))
op = input('enter an operation:  ')

if op == '+':
    print(num1 + num2)
elif op == '-':
    print(num1 - num2)
elif op == '*':
    print(num1 * num2)
elif op == '/':
    print(num1 / num2)
else:
    print('invalid')
