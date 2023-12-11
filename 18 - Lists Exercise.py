# start with empty list
things = []

# user adds 5 things to list
for i in range(5):
    things.append(input("a thing? "))

print(things)
#[a, b, c, d, e]   len==5
# 0  1  2  3  4

#Deletion phase
for i in range(2):
    index = int(input(f"an index 0-{len(things)-1}: "))
    things.pop(index)

print(things)


    