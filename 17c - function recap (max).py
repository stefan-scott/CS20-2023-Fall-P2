# Functions Re-re-re-cap  (fruitful functions)


def three_max(a, b, c):
    # this function takes 3 numbers (a,b,c)
    # and returns whichever is the largest
    if a>b:  #max is either a or c
        if a>c:
            return a
        else:
            return c
    else:    #max is either b or c
        if b>c:
            return b
        else:
            return c
#fruitful function:  1. store result in var,  2. print result out
#3. use result as input to another function
print(three_max(999, 20, 30))