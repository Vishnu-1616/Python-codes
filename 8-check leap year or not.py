# program to check leap year or not
#year-365 days
#leap year-366 days
#1996 is a leap year
#1st condition: 1996%400==0 & 1996%100==0(then leap year)
#2nd condition: 1996%4==0 & 1996%100 != 0 (then leap year)

year = int(input('Enter year: '))
if year%400==0 & year%100==0 & year%4==0:
    print('leap year')
else:
    print('not leap year')
print()
print()

#another example
year1 = int(input('Enter year: '))
if (year%400==0) and (year%100==0):
    print('leap year')
elif (year%4==0) and (year%100!=0):
    print('leap year')
else:
    print('not leap year')