import turtle

bob = turtle.Turtle()

bob.color('blue', 'turquoise') #first value is outline, second is fill

bob.begin_fill()
bob.forward(100)
bob.right(90)
bob.forward(100)
bob.right(90)
bob.forward(100)
bob.right(90)
bob.forward(100)
bob.end_fill()

#moving bob without drawing anything
bob.penup()
bob.forward(150)
bob.pendown()


bob.color('turquoise', 'blue')

bob.begin_fill()
bob.forward(100)
bob.right(90)
bob.forward(100)
bob.right(90)
bob.forward(100)
bob.right(90)
bob.forward(100)
bob.end_fill()

bob.setheading(270) #sets heading to south

bob.color('black')
bob.forward(500)



turtle.done() #keeps animation window open