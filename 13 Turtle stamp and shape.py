# A bit more about Turtle
# Mr. Scott
# Nov 23, 2023
# shape, stamp, tracer

import turtle
window = turtle.Screen()
tim = turtle.Turtle()
# turtle.tracer(False) #turns off turtle animation...

# set some turtle attributes
tim.speed(0)
tim.color("mediumspringgreen")
tim.shape("circle")  # arrow, blank, circle, classic,
tim.up()             # square, triangle, turtle.
 
# Hollow-C
def hollow_c():
    # draw a hollow c from inside corner
    small = 15
    long = 100
    medium = long-small
    
    tim.fd(medium)
    tim.left(90)
    tim.fd(small)
    for i in range(3):
        tim.left(90)
        tim.fd(long)
    tim.left(90)
    tim.fd(small)
    tim.left(90)
    tim.fd(medium)
    tim.right(90)
    tim.fd(medium-small)
    tim.right(90)

tim.pendown()
for i in range(1):
    hollow_c()
    tim.left(30)


    
    








def pattern():
    # draw a single-line pattern
    for d in range(15, 60, 5): #[15, 20, 25, 30..., 60, 65]
        tim.fd(d)
        tim.stamp()
    tim.goto(0,0)

# for i in range(180):
#     pattern()
#     tim.left(2)
# tim.color("blue")



window.exitonclick()