# Loop by Item vs Loop by Index

transport = ["airplane", "bus", "car", "dogsled", "elevator"]
#                0         1      2        3           4
#                                -3       -2          -1
#  len(transport) → 5     range(len(transport))    [0,1,2,3,4]

# LOOP BY ITEM   -> easy to code. We don't know *where*
#                   the items are located in the list
for method in transport:
    print(f"You can travel by: {method}")

# LOOPING BY INDEX -> a bit more work, but allows us to also know
#                     location in the list of each item

for index in range(len(transport)):
    current_item = transport[index]
    print(f"Item at {index}: {current_item}")
    
# Exercise: Write a function to convert a string to aLtErNaTiNg CaSe

def alt_case(str):
    # given a string of text, return the same text where
    # the case alternatives from lower to higher and so on,
    # changing at each character.    .upper()  .lower()
    # Even Char Pos:  lower   Odd Char Pos: upper
    # n % 2 == 0 for all EVEN numbers.   n % 2 == 1 for all ODD numbers
    result = ""  # accumulator variable
    for index in range(len(str)):
        letter = str[index]
        if index % 2 == 0:  #TRUE if EVEN
            result = result + letter.lower()
        else:  #must be an ODD index
            result += letter.upper()
    return result

print(alt_case("Here is some TEST TEXT"))
    
    
    

    