# num1 = 20
# num2 = 47
# num3 = 57
# sum = num1 + num2 + num3
# print(sum)

#check if the number is odd or even
# num = int(input('enter number '))
# print('number entered: ', num )
# if num % 2 == 0 :
#     print('number is even')
# else : 
#     print('number is odd')    

#Caluculate BMI
# height = float(input('enter your height'))
# weight = float(input('enter your weight'))
# BMI = weight / (height/100)**2
# print('your BMI is: ', BMI)
# if BMI<= 18.4:
#     print('you are underwight')
# elif BMI<= 24.9:
#     print('you are normal')
# elif BMI<=34.9:
#     print('your obese')
# else:
#     print('your extreme obese')
        
 #operator 111
# a = 'ambrose'
# if (type(a)is str ) :
#     print('true')
# else:
#     print('false')   


#divisibility tests
# print('enter two numbers to test divisibility')
# num1 = int(input('Num 1: ')) 
# num2 = int(input('Num 2: '))
# print(num1)
# print(num2) 
# if num1 % num2 ==0 :
#     print(str(num1)+ ' is divisible by ' + str(num2)) 
# else :
#     print(str(num1)+' is not divisible by'+ str(num2) )
       
# if num2 % 2 ==0 :
#     print(str(num2) +' is an Even number')
# else :
#     print(str(num2)+ ('is an odd number'))
                            
                            

# Choose a ride
# print('select your ride')
# print('1. bike')
# print('2. car')
# choice= int(input('enter your coice'))
# if choice== 1:
#     print('what type of bike')
#     print( '1.quad bike')
#     print('2. motorcycle')
#     choice2 = int(input('which bike do you prefer'))
#     if choice2 == 1:
#         print('you have selected a quad bike')
#     else:
#         print('you have selected a mortorcycle')
# elif choice==2:
#     print('what type of car do you want ')
#     print('1. Mercedes Benz')
#     print('2. Toyota v8')
#     choice3=  int(input('which car do you prefer'))
#     if choice3==1:
#         print('you have selected a Mercedes Benz GLE')
#     else:
#         print('you have selected a Toyota v8')                
# else:
#     print('invalid choice')        


#Reverse
# name = input('Enter your name ')
# str= ('')
# for i in name:
#     str= i + str
# print('original name ', name)
# print('reversed name ', str)  
# for n in range (45): 
#     print(n)
# for i in range (10,1000,10):
#     print(i) 
    
    
    
        #Enter number
# num =int(input('Enter any number here: '))
# sum=0
# x = 1
# while x<= num : 
#     sum = sum  + x 
#     x += 1
# print(sum, ' is the sum of all the numbers there   ')  

# g= 0
# num =int(input('enter a whole number of yuor choice: '))
# l= 2
# while l<= (num/2):
#     if (num% l ) ==0:
#         g=1
#         break
#     else:
#         l += 1
# if num == 1:
#     print('1 is not a prime number ')
# elif g == 0 :
#     print(num,'is a prime number' )    
# elif g==1 :
#     print(num ,'is not a prime numbre')
                 
#nested loops
# y=input('enter a word of your choice: ')
# x = input('enter character of yuor choice')
# i = 0 
# count = 0 
# while i <len(y):
#     if y[i]==x :
#         count+=1
#     i +=1 
# print('The total number of times ', x , 'has ocured is ', count )
    
#patterns
# print('Enter number of rows for the half pyrmid pattern (*):  ') 
# n=int(input('how many rows should it have:  '))  

# for i in range(n):
        
#         for h in range(i +1 ):
#                 print('*', end='' )
#         print()        
                
# p = int(input('Enter number of rows for the pattern : '))
# d=1 
# for i in range(1, p+1 ):
#         for v in range(1, i+1):
#                 print(d, end='')
#                 d+=1

#turtle
import turtle
# f=turtle.Screen()
# f.bgcolor ('blue')
# f.title('Turtle')
# pen=turtle.Turtle()
# size = 0 
# while True:
#         for i in range(4):
#                 pen.fd(size+1 )
#                 pen.left(90)
#                 size-=5
#         size +=1        
        
# turtle.Screen().bgcolor('navy blue')
# turtle.Screen().setup(300,400)
# polygon= turtle.Turtle()
# sides=100
# lenght=70
# angle=360.0/sides
# for i in range(sides):
#         polygon.forward(lenght)
#         polygon.right(angle)
# turtle.done()
              
# def cube(num1):
#         return num1**3
# def by3(num1):
#         if num1 % 3 ==0 :
#                 return cube(num1)
#         else:
#                 return False
# print        

a= input('Enter a word please').upper()
if 'B' in a:
        print('the word has letter b')
else:
        print ('word doesnot have letter b')         

V=10
while V > 0 :
        V-=1
        if V ==7:
                continue
        print(V)
                 