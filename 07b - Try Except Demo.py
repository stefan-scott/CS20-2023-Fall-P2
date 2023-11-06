# Try Except Demo
# Mr. Scott
# Nov 6, 2023
# To prevent our programs from crashing so much...
#          0    1      2         3 4 5

my_list = [88, 44, "Twenty Two"]       # No problem...
while True:
    try:
        index = int(input("Enter an index: ")) # int() with text → ValueError
        chosen_number = my_list[index]         # index out of bounds → IndexError
        print("Number: " + chosen_number)      # can't join number+str → TypeError
        break  #if I get here with no trouble, break out of the loop
    except TypeError:
        print("Type Error")
    except: #generic catch-all for any exception type
        print("Some sort of exception happened...")

print("the program continues...")





