# Micro:bit LED functions
# Mr. Scott
# Dec 13, 2023
# Some helper functions for working with the LED matrix

import microbit, time, random

# list to represent the 5x5 grid. 2D list
grid = [ [5, 0, 0, 0, 0],
         [0, 5, 0, 0, 0],
         [0, 0, 5, 0, 0],
         [0, 0, 0, 5, 9],
         [0, 0, 0, 0, 5] ]

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
# Main Code to test them...







# # Super Quick Recap - Built-in Images
# microbit.display.show(microbit.Image.SAD)
# # custom Images
# my_image = "11011:33033:55055:77077:99099"
# microbit.display.show(microbit.Image(my_image))