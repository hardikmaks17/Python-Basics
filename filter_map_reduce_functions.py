# Here, we will see how to work with - filter() , map() & reduce() function using lambda function.
# filter()  - the filter() method filters the given sequence with the help of a function that tests each element in the sequence to be true or not.
# map()     - this function returns a map object(which is an iterator) of the result after appliying the given function to each item of a given iterable (list,tuple etc...)
# reduce()  - the reduce() function is used to apply a particular function passed in it's arguments to all of the list elements mentioned in the sequence passed along. This function is defined in "functools" module(library).


# Sample Program - 1    :   Filter(function,iterable)


# Way - 1   :   Using def function

nums = [2,3,12,4,8,9,1,5,10,12]

def is_even(n):
    return n%2==0

# evens = set(filter(is_even,nums))                         # Gives output in form of " set "
# evens = tuple(filter(is_even,nums))                       # Gives output in form of " tuples "
evens = list(filter(is_even,nums))                          # Gives output in form of " list "

print("Even numbers using def function    :",evens)

# Way - 2   :   Using anonymous/lambda function

nums = [2,3,12,4,8,9,1,5,10,12]

# is_even = lambda n : n%2==0
# evens = list(filter(is_even(),nums))

evens = list(filter(lambda n : n%2==0,nums))                # Filter(f,v) Function
print("Even numbers using lambda function :",evens)
print()


# Sample Program - 2    :   map(function,iterable)


nums = [2,3,12,4,8,9,1,5,10,12]
evens = list(filter(lambda n : n%2==0,nums))

# Way - 1 : using def function
def update(n):
    return n*2
doubles = list(map(update,evens))
print("Mapped values using def function    :",doubles)

# Way - 2 : using lambda function
doubles = list(map(lambda n : n*2,evens))                   # Map(f,v) function
print("Mapped values using lambda function :",doubles)
print()


# Sample Program - 3    :   reduce(function,sequence)

# To use reduce function we have to import below library -
from functools import reduce

nums = [2,3,12,4,8,9,1,5,10,12]
evens = list(filter(lambda n : n%2==0,nums))
doubles = list(map(lambda n : n*2,evens))

# Way - 1 : using def function

def add_all(a,b):
    return a + b
sum = reduce(add_all,doubles)
print("Sum of all doubles using def function    :",sum)

# Way - 2 : using lambda function

sum = reduce(lambda a,b : a+b ,doubles)
print("Sum of all doubles using lambda function :",sum)