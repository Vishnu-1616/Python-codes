#program to find largest number

num1 = int(input('enter your first number: '))
num2 = int(input('enter your second number: '))
num3 = int(input('enter your third number: '))

if num1>num2 and num1>num3:
    print('the largest number is:', num1)
elif num2>num1 and num2>num3:
    print('the largest number is:', num2)
else:
    print('the largest number is:', num3)