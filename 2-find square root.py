#find square root of a number
#method-1 (using exponentiation)

num=int(input('enter your number: '))
sr = num**(1/2)
print(f'the square root of {num} is {int(sr)}')
print()
#method-2 (using math module)
import math
num1=int(input('enter your number:'))
square_root = math.sqrt(num1)
print(f'the square root of {num1} is {int(square_root)}')