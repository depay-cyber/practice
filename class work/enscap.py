

class Word:
    def __init__(self,x ):
        self.x=x 
    
    def reverse(self):
        return self.x[::-1]
word = input('Enter a word to reverse: ') 
obj= Word(word)
r=obj.reverse()
print(r)         
            
