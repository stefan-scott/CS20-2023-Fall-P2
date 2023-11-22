# Turtles and Regular Polygons
# Mr. Scott
# Nov 22, 2023
# Creating some functions and looking at generalization

# Start with Turtle Boilerplate code
import turtle
window = turtle.Screen()
roscoe = turtle.Turtle()
roscoe.speed(40)
turtle.tracer(False)

# Function Definitions
def triangle(length):
    # uses the turtle to draw an equilaterial triangle
    # length → INT → used for the triangle side length
    for i in range(3):  #repeat 3   [0,1,2]
        roscoe.fd(length)
        roscoe.left(120)
        
def square(length):
    # same as above, but for a square
    for i in range(4):
        roscoe.fd(length)
        roscoe.left(90)

def pentagon(length):
    # same as above, but for pentagon
    for i in range(5):
        roscoe.fd(length)
        roscoe.left(72)

def r_poly(x, y, s):
    # draw a regular polygon with the turtle
    # x → INT → x-coordinate for the turtle's start position
    # y → INT → y-coordinate  ""
    # s → INT → number of side
    roscoe.up()
    roscoe.goto(x,y)
    roscoe.down()
    
    for i in range(s):
        roscoe.fd(300/s)
        angle = 360/s  #always yields the external angle for reg. poly.
        roscoe.left(angle)
# Run the functions
r_poly(-250,0,6)
r_poly(0,0,10)
r_poly(250,0,200000)



# pentagon(100)



# for i in range(0,360,3): #[0,3,6,9,12....345, 350, 355]
#     square(i)
#     roscoe.left(3)




# for i in range(20, 200, 5):  #[20, 25, 30, 35, ..., 195]
#     triangle(i)

window.exitonclick()
