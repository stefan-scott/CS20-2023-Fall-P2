# Micro:bop:it Starter
# Mr. Scott
# Dec 14, 2023
# Detecting "SHAKE" + start for game project

import microbit, time, random

choices = ["A", "B", "S"]  #could add more actions (tilt)
target_action = random.choice(choices)

# MAIN LOOP
while True:
    #First, display the target action
    microbit.display.show(target_action)
    
    # CHECK FOR USER INPUT
    action = microbit.accelerometer.get_z()
    # 1. Check for "SHAKE"
    if action < -1300 or action > 1300: # Means a SHAKE happens
        print("SHAKE!")
        time.sleep(0.5) #a no "shake detect" buffer time
        
        if target_action == "S":  #user was correct
            print("CORRECT!")
            # reset timer, play an icon/animation to show user was correct
            target_action = random.choice(choices)
        else:
            print("Incorrect - GAME OVER")
            
    # 2. Check for button A
    # 3. Check for button B
    time.sleep(0.1)
    
    
    
    
    