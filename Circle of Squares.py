import turtle
mandu=turtle.Turtle()


def square(angle):
    mandu.forward(100)
    mandu.right(angle)
    mandu.forward(100)
    mandu.right(angle)
    mandu.forward(100)
    mandu.right(angle)
    mandu.forward(100)
    mandu.right(angle+10)
    #mandu.forward(100)

for i in range(36):
    square(90)

           
