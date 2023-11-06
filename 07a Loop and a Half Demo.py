# Loop-and-a-half
# Mr. Scott
# Nov 6, 2023
# "Forever" loop + break and continue

# DO TYPE THIS ☻↓☻☻♥▼
while True:  #infinite loop     
    choice = input("should we stop the loop? [yes/no]: ") #YES, YeS, yES
    if choice.lower() == "yes":
        confirm = input("are you sure?? [yes/no]: ")
        if confirm.upper() == "YES":
            break  # exits the current loop
        else:
            continue  # restarts the loop
    print("let's ask again...")
    
    