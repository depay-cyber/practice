#Lets check if you know the alphabet
print('Hi')
character  =str(input('Type in any keyboard character to check if its an alphabet letter'))
print('character typed: ', character)
alphabet =('abcdefghijklmnopqrstuvwxyz') 
if (character.lower() in alphabet):
    print('good, its part ')
else:
    print('try again you failed')    

