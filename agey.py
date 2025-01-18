try:
    year= (input('Enter your birth month and year seperated by commas '))
    print(year)
except(SyntaxError) :
    print('invalid input') 
except(NameError):
    print('wrong try again')      

