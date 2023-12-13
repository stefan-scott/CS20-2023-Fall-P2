# Micro:bit LED functions
# Mr. Scott
# Dec 13, 2023
# Some helper functions for working with the LED matrix

import microbit, time, random

# list to represent the 5x5 grid. 2D list
grid = [ [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0] ]

# LED Helper Functions
def print_grid():
    # prints our grid in an easy-to-read format
    for row in grid:
        print(row)

def show_grid():
    #convert our 2D list to a string, and display
    result = ""
    for row in grid:
        for pixel in row:
            result += str(pixel)
        result += ":"
    result = result[:-1]
    print(result)
    microbit.display.show(microbit.Image(result))
    
def set_pixel(x,y,intensity):
    #set a pixel at (x,y) to brightness: intensity(0-9)
    grid[y][x] = intensity
    show_grid()

def queue_pixel(x,y,intensity):
    #queue up a change for pixel at (x,y)
    grid[y][x] = intensity

def plot(x,y):
    #turn on pixel at x,y
    set_pixel(x,y,9)
    
def unplot(x,y):
    #turn off pixel at x,y
    set_pixel(x,y,0)
    
def set_all(intensity):
    #turn all pixels to a particular intensity
    for x in range(5):  #x → 0, 1, 2, 3, 4
        for y in range(5):  # y → 0, 1, 2, 3, 4
            queue_pixel(x,y,intensity)
    show_grid()
    
# Main Code to test them...

#1. Fading Animation
# while True:
#     for i in range(10):
#         set_all(i)
#         time.sleep(0.05)
#     for i in range(8,0,-1):
#         set_all(i)
#         time.sleep(0.05)

#2. Basic Game Mechanic - Player movement
set_all(0)  #clear the screen
player_x = 2
player_y = 4

plot(player_x, player_y)

while True:
    if microbit.button_a.was_pressed():
        if player_x > 0: #there is room to move left
            unplot(player_x, player_y)
            player_x = player_x - 1
            plot(player_x, player_y)
            
    if microbit.button_b.was_pressed():
        if player_x < 4: #there is room to move right
            unplot(player_x, player_y)
            player_x += 1
            plot(player_x, player_y)
            
    




# # Super Quick Recap - Built-in Images
# microbit.display.show(microbit.Image.SAD)
# # custom Images
# my_image = "11011:33033:55055:77077:99099"
# microbit.display.show(microbit.Image(my_image))