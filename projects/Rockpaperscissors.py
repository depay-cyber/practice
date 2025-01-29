print('Welcome torock paper scissors app')
import random
user=input('rock , paper or scissors:')
possible_actions=('rock','paper','scissors')
comp=random.choice(possible_actions)
print('your selected',user)
print('computer selected', comp)
score=0
while True:
    if comp==user:
        print('its a draw')
        score+=1
        print('your new score is',score)
        
    elif comp=='paper' :
        if user=='rock':
            print('comp wins')
            score-=2
            print('your new score is ',score) 
         
    elif comp=='rock' :
        if user=='scissors':
            print('comp wins')
            score-=2
            print('your new score is ',score)   
          
    elif comp=='scissors' :
        if user=='paper':
            print('comp wins')
            score-=2
            print('your new score is ',score)
        
    if user=='paper' :
        if comp=='rock':
            print('You wins')
            score+=3
            print('your new score is ',score) 
         
    elif user=='scissors' :
        if comp=='paper':
            print('You wins')
            score+=3
            print('your new score is ',score) 
           
    elif user=='rock' :
        if comp=='scissors':
            print('You win')
            score+=3
            print('your new score is ',score)
        
    else:
        print('error 44')   
           
    break