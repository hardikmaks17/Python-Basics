# Recursion means calling function from the same function.
# In other words, we can say recursion means function calling itself !


# Sample Program - 1    :   Recursion


def greet():
    print( "Hello!" )
    greet()

greet()


# Sample Program - 2    :   to change limit of the recursion


import sys

sys.setrecursionlimit(2000)                                     # To increase limit of the recursion
print( "limit of recursion :",sys.getrecursionlimit() )         # To cheak limit of the recursion

i = 0
def greet():

    global i
    i+=1
    print( "Hello!" , i )
    greet()

greet()
