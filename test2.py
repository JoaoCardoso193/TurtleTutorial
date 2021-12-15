import turtle
import math

bob = turtle.Turtle()
bob.speed(200) #change speed

turns = 100
angle = 137

outline_color = 'yellow'
fill_color = 'orange'

bob.color(outline_color, fill_color)

bob.begin_fill()
for i in range(turns):
    bob.forward(100)
    bob.right(angle)
bob.end_fill()




turtle.done()