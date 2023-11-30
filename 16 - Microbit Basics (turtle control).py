# Microbit Basics
# Mr. Scott
# Nov 30, 2023

import microbit, time, turtle

w = turtle.Screen()
t = turtle.Turtle()
# ACCELEROMETER - measures the orientation (acceleration) x, y, z
while True:
    x = microbit.accelerometer.get_x()
    t.fd(10)
    # -1024          0           1024
    #  LEFT     |   FLAT    |   RIGHT
    #         -300         300
    if x < -300:
        print("LEFT")
        t.left(10)
    elif x > 300:
        print("RIGHT")
        t.right(10)
    else:
        print("FLAT")
    
    
    
# # DISPLAYING TEXT (show, scroll)
# for letter in "SASK":  #show
#     microbit.display.show(letter)
#     time.sleep(0.5)
# 
# microbit.display.scroll("abcde") #ayyad +2




# microbit.display.show("A")

# could not get a prompt error
# press RESET button, then re-run the program

# need the library? TOOLS→ MANAGE PACKAGES    "cs20-microbitio"