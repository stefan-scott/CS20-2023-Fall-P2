# First Turtle Program
# Mr. Scott
# Nov 20, 2023
# How to import and utilize the turtle library
# NOTE: do NOT save your file as turtle.py

import turtle  #look for a file called "turtle.py", and load its contents

moves = int(input("enter a number of moves: "))

# boilerplate code → "startup code for using the turtle"
window = turtle.Screen()  #creates a screen object, store in variable: window
window.bgcolor("darkseagreen")

alex = turtle.Turtle()  #creates a turtle object, store in variable: alex
alex.color("yellow")    #change pen color
alex.pensize(5)         #set pen thickness to 5 pixels
alex.speed(0)   #high number is faster, but 0 is max

#PROGRAM THREE - using a loop
for i in range(moves):  #[0,1,2,3,4,5,6...  (moves-1)
    alex.forward(i)
    alex.left(45)
    
window.exitonclick()    # waits for the user to click the canvas, then close.

# PROGRAM TWO# give a few more instructions
# alex.backward(150)  
# alex.left(57)
# alex.forward(70)
# alex.goto(0,0)

# PROGRAM ONE - basic movement
# alex.forward(100)  #forward 100 units
# alex.right(45) #turn right 45 degrees
# alex.backward(200) #backward 200 units



