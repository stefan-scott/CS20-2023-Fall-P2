# Yahtzee
# Create a function called roll() that simulates rolling 5 6-sided dice. 
# Inside the function, print out the value of each rolled die. If a Yahtzee
# (all five dice the same) has occurred, print out “Yahtzee!”
import random

dice = [0, 0, 0, 0, 0]  #placeholder values
#       0  1  2  3  4
num_rolls = 0

def roll():
    # update the values in our array to simulate rolling 5 dice
    for i in range(5):  #[0,1,2,3,4]
        dice[i] = random.randint(1,6)  #1,2,3,4,5,6

def yahtzee():
    #check if we have a yahtzee, return true in that case
    if dice[0]==dice[1] and dice[1]==dice[2] and dice[2]==dice[3]and dice[3]==dice[4]:
        return True
    else:
        return False

while True:
    roll()
    num_rolls +=1
    if yahtzee():  #yahtzee()==True
        break
print(f"That took {num_rolls} rolls to get a yahtzee")