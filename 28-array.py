# How to use/import array in PYTHON
# Syntax : array('type',values)

# 'i' - signed integer      : it will allow to use all integer including -ve numbers
# 'I' - unsigned integer    : it will allow to use only +ve numbers
# 'u' - unsigned integer    : it will allow to use characters only
# 'f' - unsigned integer    : it will allow to use float values
# 'd' - unsigned integer    : it will allow to use double values


# Sample Program - 1   :   How to create array


# Way - 1

import array
vals = array.array('i',[2,5,91,50])
print("Way - 1 to import Array : ",vals)
print()

# Way - 2

import array as arr
vals = arr.array('i',[2,5,91,50])
print("Way - 2 to import Array : ",vals)
print()

# Way - 3                                                               # Prefer this syntax for every library

from array import *
vals = array('i',[2,5,91,50])
print("Way - 3 to import Array : ",vals)
vals.reverse()                                                          # function to get reverse of the array   #it is written value so can't write directly in print()
print("Reversed array :",vals)
print("\nAddress and the Size of the array :",vals.buffer_info())       # function to get address and the size of the array
print("Type of the array :",vals.typecode)                              # function to get type of the array
print()


# Sample Program - 2   :   To get values from the array individually


# Way - 1
from array import *
vals = array('i',[2,5,91,50])
for i in vals:                                                          # Directly using variable name
    print("elemnt of the array :",i)
print()

# Way - 2
from array import *
vals = array('i',[2,5,91,50])
for i in range(len(vals)):                                              # Using range() function
    print(i+1,"element of the array :",vals[i])
print()


# Sample Program - 3   :   For character type array


from array import *
vals = array('u',['b','a'])
for i in range(len(vals)):
    print(i+1,"element of the array :",vals[i])
print()


# Sample Program - 4   :   Creating new array from the existing array


from array import *

vals = array('i',[2,5,91,50])
newArr = array(vals.typecode,(a for a in vals))
for i in range(len(vals)):
    print(i+1,"element of the array :",vals[i])
print()


# Sample Program - 5   :   Creating new array from the existing array with some operations on it


# Way - 1 : Using For Loop
from array import *
vals = array('i',[2,5,9,11])
newArr = array(vals.typecode, (a*a for a in vals))                          # a*a ,, we can use other opertaions also like a*2,a%5 etc...
for i in range(len(newArr)):
    print(i+1,"element of the new array :",newArr[i])
print()

# Way - 2 : Using While Loop
i = 0
while i < len(newArr):
    print(newArr[i])
    i+=1
