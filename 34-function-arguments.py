# In Python, we don't have the concept of 'pass by value' or 'pass by reference'.
# Instead, we have immutable or mutable arguments passed to the function.
# If we pass immutable objects like integer or string to function and try to update their value, their original value will not be updated instead a new variable will be created with updated value at new memory address.
# If we pass mutable objects like list or dictionary and try to update them, their original value will be updated at the same memory address.
# Below are the sample programs.



# Sample Program - 1    :   Immutable object as argument - Integer


def update(x):
    print('Value of x before update :',x)
    print('Memory Address of x before update :',id(x))
    x=8
    print('Value of x after update  :',x)
    print('Memory Address of x after update  :',id(x))

a=10
print('Value of a before update :',a)
print('Memory Address of a before update :',id(a))
update(a)
print('Value of a after update  :',a)
print('Memory Address of a after update  :',id(a))
print()


# Sample Program - 2    :   Mutable object as argument - List


def update(x):
    print('inside function, before update :',spam)
    print('Memory address of list inside function, before update :',id(spam))
    spam[1]=-3
    print('inside function, after update  :',spam)
    print('Memory address of list inside function, after update  :',id(spam))


spam=[1,2,3]
print('Items in list :',spam)
print('Memory address of list:',id(spam))
update(spam)
print('Items in updated list :',spam)
print('Memory Address of updated list :',id(spam))
