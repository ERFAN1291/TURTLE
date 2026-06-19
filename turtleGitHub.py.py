import turtle

t = turtle.Turtle()

# test code for GitHub 

t.penup()
t.goto(-100 , 50)     # this is so the rectangle is centered.
t.color("red")
t.pendown()


for i in range(2) :
    t.pensize(5)
    t.forward(200)
    t.right(90)
    t.forward(100)
    t.right(90)
     
turtle.done()
