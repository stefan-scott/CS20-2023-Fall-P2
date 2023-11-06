# Python String Methods and if/elif/else
# Mr. Scott
# Nov 3. 2023
# A look at some new string methods, and a review of conditionals

def shirt_selection(clothing_type):
    # get some feedback on what sort of day to wear clothing on
    # clothing type → STR ("t-shirt", "bunnyhug", "jacket")
    if clothing_type.lower() == "t-shirt":
        print("Warm Summer Day")
    elif clothing_type.upper() == "BUNNYHUG":
        print("Cool Fall Day")
    else:
        print("Cold Winter Day")
        
shirt_selection("bunNyHug")
# NOTES / CONTENT
# String Methods
#     .upper() → returns string as all uppercase characters
#     .lower() → returns string as all lowercase characters
#     .capitalize() → returns string, lowercase except 1st char

#   = → assignment operator (store value in variable)
#  == → equality comparison (are two things equal)

