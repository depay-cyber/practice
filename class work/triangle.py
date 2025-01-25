import turtle
turtle.Screen().bgcolor('orange') 
turtle.Screen().setup(300, 400)
pen=turtle.Turtle()
size = 0 
while True:
        for i in range(3):
                 pen.fd(size+1 )
                 pen.left(90)
                 size-=5
         size +=1        