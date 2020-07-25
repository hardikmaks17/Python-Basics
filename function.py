# Here, We will learn how to create function.

# Syntax    :   def function_name():


# Sample Program - 1    :   How to create function.


def function():

    print("Hello")
    print("Good Evening!")
# Above we have successfully created function. but we can not get any output here because we are not calling it.
# Below line we are calling our first function and we will get output now.
function()

# We can also get/call our function multiple times in our program.

function()
print()


# Sample Program - 2    :   Creating function for addition

def add(x,y):                                   # we can call x & y as arguments(paramiters)
    c = x + y
    #print("Addition of two numbers :",c)
    return c

result = add(7,9)
print("Addition of two numbers :",result)
print()


# Sample Program - 3    :   Creating function for addition and substration both

def add_sub(x,y):
    #x = int(input("Enter first number :"))
    #y = int(input("Enter second number :"))
    a = x + y
    s = x - y
    return a,s

result1,result2 = add_sub(5,4)                  # we have returned two values a & s,, so we have to accept two values also... So i have written result1 & result2
print("Addition :",result1,"\nSubstraction :",result2)