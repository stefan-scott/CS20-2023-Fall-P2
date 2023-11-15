# Using PySimpleGUI for input/output DEMO
# Mr. Scott
# Nov 15, 2023
# Looking at an alternative to input() and print()

import PySimpleGUI as sg  #alias sg → "Simple Gui"

# Reading a string from the user:
name = sg.popup_get_text("Enter a name:")
# can check if the user pressed Cancel or X
if name==None:
    print("pressed Cancel or X")
    
# Printing out some string data on a popup
greeting = "Hello, " + name + " nice to see you!"
sg.popup(greeting)
sg.popup(greeting, title="TEST",background_color="black")


