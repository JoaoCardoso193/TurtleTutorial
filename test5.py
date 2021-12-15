import turtle

bob = turtle.Turtle()
screen = bob.getscreen()
bob.speed(1000)

print(turtle.screensize())

screen.bgcolor('light blue')

bob.penup()
bob.goto((0, 100))
bob.pendown()

def star(turtle, size):
    if size <= 10:
        return
    else:
        for i in range(5):
            bob.forward(size)
            star(turtle, size/4)
            bob.right(144)

star(bob, 200)

turtle.done()