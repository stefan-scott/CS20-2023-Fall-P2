# Microbit Buttons and Images
# Mr. Scott
# Dec 11, 2023
# Different button interactions + Images/Animations

import microbit, time

# Images - slideshow 
microbit.display.show(microbit.Image.PITCHFORK)
time.sleep(1)

microbit.display.show(microbit.Image.GHOST)
time.sleep(1)

# Animation - clock
clock_image = [microbit.Image.CLOCK1,
               microbit.Image.CLOCK2,
               microbit.Image.CLOCK3,
               microbit.Image.CLOCK4,
               microbit.Image.CLOCK5,
               microbit.Image.CLOCK6,
               microbit.Image.CLOCK7,
               microbit.Image.CLOCK8,
               microbit.Image.CLOCK9,
               microbit.Image.CLOCK10,
               microbit.Image.CLOCK11,
               microbit.Image.CLOCK12]
index = 0
delay = 0.2 #animation speed
while True:
    microbit.display.show(clock_image[index])
    index += 1  #0 1 2 3 4 5 6 7 8 9 10 11 NONONO
    #index = index + 1
    if index > 11:
        index = 0
    #button press code ... was_pressed()
    
    time.sleep(delay) 

# 1. Functions Practice Quiz
# 2. Add button detection to our code above:
#   A → slows down the animation
#   B → speed up the animation



# # Button Interactions (2 ways..both are Boolean Functions)
# button_a_count = 0
# button_b_count = 0
# 
# microbit.display.show("A")
# time.sleep(2) #2 second delay to simulate some work being done
# microbit.button_b.was_pressed()  #True | False
# 
# while True:
#     if microbit.button_a.is_pressed():  #good for detecting a HOLD
#         button_a_count += 1 #button_a_count = button_a_count + 1
#         
#     if microbit.button_b.was_pressed(): #good for detecting SINGLE PRESS
#         #only true if button was pressed SINCE last was_pressed()
#         button_b_count += 1
#         
#     print(f"a: {button_a_count} \t b: {button_b_count}")



