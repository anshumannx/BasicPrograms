import turtle

flo=turtle.Turtle()
flo.speed(10)
flo.color("yellow","pink")
flo.begin_fill()
for i in range(150) :
    flo.forward(300)
    flo.left(170)

flo.end_fill()
turtle.done()