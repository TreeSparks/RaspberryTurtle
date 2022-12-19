import turtle

WOOD_COLOR = 'white'
LEAVES_COLOR = 'green'
BACKGROUND_COLOR = 'black'

t = turtle.Turtle()
t.screen.bgcolor(BACKGROUND_COLOR)
t.pensize(2)
t.color('green')
t.left(90)
t.backward(100)
t.speed(0) # 1-10 (0 turns off animation and goes fast as possible)
#t.shape('turtle')
def tree(i):
    if i<10:
        return
    else:
        t.forward(i)
        t.color(LEAVES_COLOR)
        t.circle(2)
        t.color(WOOD_COLOR)
        t.left(30)
        tree(3*i/4)
        t.right(60)
        tree(3*i/4)
        t.left(30)
        t.backward(i)
tree(100)
turtle.done()
