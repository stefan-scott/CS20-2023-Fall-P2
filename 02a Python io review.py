# I/O Python Review
# Mr. Scott
# October 30, 2023
# input(),  output(),  data types / conversions

# OUTPUT - printing to shell SIMPLE (one piece of data)
print(99)  		#print a number
print("hello")  #print a string literal
text = "CS20"   # set text to "cs20"
print(text)    # [alt]026  →  

# OUTPUT lv2 - printing multiple things...at once
print("Hello" + text) # STR+STR  → concatenation/join
print("Hello" , text , "!") # printing with , → joins with added space ch

# OUTPUT lv3 - printing strings and numbers (mixed types)
num = 45
#         STR          INT
print("best number:" , num) #print mixed types easily, one at a time
print("best number:" + str(num)) #need str() to convert INT to STR


# INPUT - reading in values and storing in variables
number_one = input("enter a number: ")  #INPUT → STR
number_two = input("enter another number: ")  #INPUT → STR

# DO MATH? Convert to a numeric form...
number_one = float(number_one)
number_two = float(number_two)

#FLOAT     FLOAT      FLOAT
result = number_one + number_two
#         STR           STR
print("The sum is: " + str(result))


# What if we wanted to multiply?? Use *
print(5*9)



