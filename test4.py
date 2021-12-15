import turtle

bob = turtle.Turtle()
screen = bob.getscreen()

screen.bgcolor('blue')
turtle.color('black', 'white')

turtle.begin_fill()
for i in range(5):

    turtle.forward(100)
    turtle.right(144)
turtle.end_fill()


turtle.done()