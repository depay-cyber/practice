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
print('enter two numbers to test divisibility')
num1 = int(input('Num 1: ')) 
num2 = int(input('Num 2: '))
print(num1)
print(num2) 
if num1 % num2 ==0 :
    print(str(num1)+ ' is divisible by ' + str(num2)) 
else :
    print(str(num1)+' is not divisible by'+ str(num2) )
       
if num2 % 2 ==0 :
    print(str(num2) +' is an Even number')
else :
    print(str(num2)+ ('is an odd number'))
                            