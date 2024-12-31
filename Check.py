y=input('enter a word of your choice: ')
x = input('enter letter you want to check out in the word')
i = 0 
count = 0 
while i <len(y):
    if y[i]==x :
        count+=1
    i +=1 
print('The total number of times ', x , 'has ocured is ', count )
    