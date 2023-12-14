# Timer Demo
# Mr. Scott
# Dec 14, 2023
# Using time library to simulate a stopwatch

import time, microbit

# time.sleep(s)  → inserts a delay of s seconds
# time.time() → return to us the current time since the epoch...
# epoch → Jan 1, 1970 0:00 UTC
# game: press a button at least once per 5 seconds...

start_time = time.time()  #snapshot time
while True:
    current_time = time.time()  #constantly updated
    elapsed_time = current_time - start_time
    
    print(elapsed_time)
    if microbit.button_a.was_pressed():
        start_time = time.time()
    
    if elapsed_time > 5:
        print("You forgot to press A!")
        break
#     print(f"s: {start_time} \t c: {current_time}")