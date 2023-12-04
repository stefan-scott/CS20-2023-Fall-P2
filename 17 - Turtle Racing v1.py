# Turtle Racing v1
# Mr. Scott
# Dec 4, 2023

import random, turtle

# RANDOM:  random.randint(low,high)  random.uniform(low,high) Float,   random.choice(list)

#Set up window and some turtles
w = turtle.Screen()
w.bgcolor("lightblue")

lance = turtle.Turtle()
andy = turtle.Turtle()
lance.shape("turtle")
andy.shape("turtle")
lance.color("blue")
andy.color("red")

# Go to the starting Line
lance.up()
andy.penup()
lance.goto(-250, 20)
andy.goto(-250, -20)

# Race! 4 Different Types...

# Race1 → Single Random Number (dist)
# lance.fd(random.randint(100,500))
# andy.fd(random.randint(100,500))

# Race2 → Loop a random # of times, fixed distance
# for i in range(random.randint(20,100)):
#     lance.fd(5)
# 
# for j in range(random.randint(20,100)):
#     andy.fd(5)

# Race3 → One loop, moving in tiny little slices
# for i in range(150):
#     andy.fd(random.randint(1,6))  #1-6 pixels
#     lance.fd(random.randint(1,6)) #1-6 pixels

print(f"Lance's position: {lance.xcor()}, {lance.ycor()}")
print(f"Andy's position: {andy.xcor()}, {andy.ycor()}")

finish_line = 200  #x-position
while lance.xcor() < finish_line and andy.xcor() < finish_line:
    andy.fd(random.randint(3,6))
    lance.fd(random.randint(3,6))

#Determine the winner
if lance.xcor() < andy.xcor():
    print("Andy (Red) Wins!!")
elif lance.xcor() > andy.xcor():
    print("Lance (Blue) Wins!!")
else:
    print("Tie!!")


w.exitonclick()