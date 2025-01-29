print('Hi lets check your pasword strenght')
pasw=input('Enter yuor password: ')
alphabet=('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
coplx=('!@#$%^&*:?/+~')
num=('123456789')
n=0
y=0
u=0
m=0
for i in pasw:
    if len(pasw)>=6:
        n+=3
    if i in alphabet:
        y+=2
    if i in coplx:
        u+=3
    if i in num:
        m+=2 
          
total=n+y+u+m  
strength=total*10
print('Your pasword strength is',strength,'%')             
