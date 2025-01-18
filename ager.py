try:
    year= int(input('Enter your birth  year  '))
    print('Birth year is', + year)
except(SyntaxError) :
    print('invalid input') 
except(NameError):
    print('wrong try again')
except(ValueError):
    print('wrong values boss, try again ') 
age= 2025 - year
if age < 0 :
    print('Error , Error 67 occured') 
else:
    print('Your age is', + age)                

