import turtle
f=turtle.Screen()
f.bgcolor ('blue')
f.title('Turtle')
pen=turtle.Turtle()
size = 0 
while True:
    for i in range(4):
        pen.fd(size+1 )
        pen.left(90)
        size-=5
        size +=1        