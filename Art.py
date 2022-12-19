import turtle 

t = turtle.Turtle()
t.screen.bgcolor('black')
t.color('purple')
t.pensize(2)
t.speed(0)

for i in range(0,4):
    t.forward(100)
    t.right(90)

turtle.done()
