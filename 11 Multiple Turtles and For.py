# Multiple turtles and for loops
# Mr. Scott
# Nov 21, 2023
# A look at multiple instances of turtles, and controlling them

import turtle

wn = turtle.Screen() #create a window/canvas

#Create the turtles
frank = turtle.Turtle()
frank.pensize(4)
frank.color("pink")

martha = turtle.Turtle()
martha.pensize(2)
martha.color("brown")

turtle_list = [martha, frank]  #empty list to put the turtles into
turtle_list.append(turtle.Turtle()) #append → to add onto the end of...
color_list = ["blue", "mediumspringgreen", "cadetblue", "lavender"]

color_index = 0

# Use for loops to control our turtles
turtle_list[0].left(120)
turtle_list[1].right(120)

for distance in range(50, 10, -1): #[50, 48, 46, 44...., 16, 14, 12]
    for current_turtle in turtle_list:
        current_turtle.color(color_list[color_index])
        current_turtle.speed(0)
        current_turtle.fd(distance)
        current_turtle.rt(20)
    #now cycle color
    color_index = color_index + 1
    if color_index > 3:
        color_index = 0 #wrap around back to the first color



# #PROGRAM TWO - Control the turtles
# #First, frank
# frank.forward(150)
# frank.lt(40)  #.left()  .lt()
# frank.fd(50) #.forward()  .fd()
# 
# #Reposition Martha
# martha.up() #.penup()  .up()
# martha.back(200)
# martha.down() # .pendown()  .down()
# 
# #Second, Martha
# martha.forward(150)
# martha.left(40)
# martha.fd(50)

# # FOR Loops Recap
# #             0        1           2              3
# my_list = ["apple", "banana", "cantaloupe", "dragon fruit"]  
# 
# #for    loop var       in     collection
# for        item        in    my_list:     #repeat 4
#     print(f"I'd like to buy a(n) {item}")
# 
# for letter in "Saskatchewan":     #repeat 12
#     print(letter)
#     
# for i in range(10):   #[0,1,2,3,4,5,6,7,8,9]   repeat 10
#     print("num", i)

