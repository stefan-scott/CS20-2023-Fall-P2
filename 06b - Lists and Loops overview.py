# Python Super Basics Demo
# Mr. Scott
# Nov 3, 2023
# Overview of Lists and Loops

# LISTS
foods = ["apple", "banana", "cantaloupe", "starfish"]
#          0         1          2             3          4??
#          -4       -3          -2            -1

# length of a list using len()
# print(len(foods))

# LOOPS - Conditional (while) Loop
current_num = 0
while current_num < 15:
    print(current_num)
    current_num += 1  #current_num = current_num + 1    -=  *=  /=

print("--------")

# LOOPS - Counting (for) Loops  ... Loops over a collection (List, String)
#   loop var         collection
for   fruit     in   foods:   #repeat 4
    print(fruit)

print ("-----")

for letter in "WINTER":   #repeat 6
    print(letter)

print ("-----")

# range(10) → [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# range(5, 10) → [5, 6, 7, 8, 9]
# range(2, 20, 4) → [2, 6, 10, 14, 18]

for i in range(2, 20, 4):
    if i == 6:
        print("SIX")
    else:
        print(i)

#Student Challenges:
#1. Using a while loop, print out the numbers 100, 90, 80, ..., 20, 10, 0.
count = 100
while count >= 0:
    print(count)
    count -= 10   #count = count - 10


#2. Write a for loop that repeats 6 times. Design a code body so that the following is printed out:
for i in range(6):  #0,1,2,3,4,5
    if i < 3:
        print("Go!")
    else:
        print("Chargers!")


# Go!
# Go!
# Go!
# Chargers!
# Chargers!
# Chargers!


# 3. Using a for loop, print out the numbers from 0 to 30 (counting by 5s)
# but DON'T print out 15!


