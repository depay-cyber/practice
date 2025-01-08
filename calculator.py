# print('lets divide by 2')
# num=int(input('enter the number: '))
# ans= num/2
# print (ans)
def add(num1, num2):
    return(num1 + num2)
def subtract(num1 , num2):
    return(num1 - num2)
def divide(num1, num2):
    return(num1 / num2)
def multiply(num1,num2):
    return(num1/ num2)
print ('please select the operation')
print('a. add, n\ b. subtract ,n\c. divide, n\d.  multiply ')
choice=input('Please emter choice a or b or c or d ')
num1 =int(input('Please enter the firt number'))
num2=int(input('please enter second number'))
if choice=='a':
    print(num1 , '+', num2, '=', add(num1, num2))
elif choice=="b":
    print(num1 , '-', num2, '=', subtract(num1, num2))
elif choice == 'c':
    print(num1 , '/', num2, '=', divide(num1, num2)) 
elif choice== 'd':
    print(num1 , '*', num2, '=', multiply(num1, num2)) 
else:
    print('invalid input')
             
    




