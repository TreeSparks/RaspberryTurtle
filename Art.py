import turtle

t = turtle.Turtle()

ANGLE = 4
BACKGROUND_COLOR = 'black'
CIRCLE_COLOR = 'green'

t.screen.bgcolor(BACKGROUND_COLOR)
t.pensize(2)

t.speed(0)
t.left(90)
t.color(BACKGROUND_COLOR)
t.forward(100)
t.right(90)

t.color(CIRCLE_COLOR)
for i in range(0,int(360/ANGLE)):
    t.forward(12)
    t.right(ANGLE)

turtle.done()
