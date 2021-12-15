import turtle
import math

bob = turtle.Turtle()
bob.color('black', 'yellow')
bob.speed(1000)


bob.begin_fill
for i in range(900):
    bob.forward(math.sqrt(i))
    bob.left(i%180)
bob.end_fill

turtle.done()