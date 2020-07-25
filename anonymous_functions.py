# Functions without name can be called as anonymous functions or lambda.
# functions are objects in Python.
# Yor can pass any number of arguments in lambda function but it should be only in one expression (ie, a*a,a*b,a+b ...).


# Sample Program - 1    :   Square of a given number

f = lambda a : a * a


# Input by user
x = int(input("Enter a number : "))
result = f(x)

# result = f(5)                                     # By default input

print("Square of the number :",result)
print()


# Sample Program - 2    :   Addition of given numbers

m = lambda a,b : a + b

# Input by user
x,y = int(input("Enter first number : ")) , int(input("Enter second number : "))
result = m(x,y)

# result = m(2,3)                                     # By default input

print("Addition of the two numbers :",result)