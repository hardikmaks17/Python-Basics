# Different operations on the array


# Sample Program - 1    :   Adding values in each element of the array


# Way - 1   :   by using for/while loop

# Way - 2   :   direct
from numpy import *

arr = array( [1, 5, 9, 3, 4, 6] )
arr = arr + 5
print( arr )
print()

# Sample Program - 2    :   Addition of two array  (We can say this as vectorized operation)     # Note - Both array should have same number of values


from numpy import *

arr1 = array( [1, 2, 3, 4, 5] )
arr2 = array( [1, 5, 9, 3, 8] )
arr3 = arr1 + arr2
print( "Addition of two array :", arr3 )
print()

# Sample Program - 3    :   Operations on array


from numpy import *

arr = array( [1, 5, 9, 3, 4, 6] )
arr = arr + 5
print( arr )
print( "sine value of each element : ", sin( arr ) )
print( "cos value of each element :", cos( arr ) )
print( "log value of each element :", log( arr ) )
print( "Square Root value of each element :", sqrt( arr ) )
print( "sum of the all elements of the array :", sum( arr ) )
print( "Minimum value of the array :", min( arr ) )
print( "Maximum value of the array :", max( arr ) )
print()
# Above we can use other maths functions also like tan,sqrt etc...


# Sample Program - 3    :   Concatenation of two arrays


from numpy import *

arr1 = array( [1, 2, 3, 4, 5] )
arr2 = array( [1, 5, 9, 3, 8] )
print( "Concatenation of two arrays :", concatenate( [arr1, arr2] ) )
print()

# Sample Program - 4    :   Copying array

# Way - 1   :   scintifically this is not copying ,, WE CAN CALL THIS METHOD AS "ALIASING"
from numpy import *

arr1 = array( [5, 12, 36, 47, 81] )
arr2 = arr1
print( arr1 )
print( arr2 )
print( "Addres of arr1 :", id( arr1 ) )
print( "Addres of arr2 :", id( arr2 ) )
print()

# Way - 2   :   right way
from numpy import *

arr1 = array( [-5, 47, 78, 15, 42] )
arr2 = arr1.view()
print( arr2 )
print( "Addres of arr1 :", id( arr1 ) )
print( "Addres of arr2 :", id( arr2 ) )
print()

# Sample Program - 5    :   There is two type of copying array.  1] Shallow Copy     2] Deep Copy

# 1] Shallow Copy - Both array are dependent on each array always. like if I change one of the array's element than other array will also change.

from numpy import *

arr1 = array( [1, 8, 6, 4, 0, 3, 9] )
arr2 = arr1.view()
arr1[2] = 7
arr2[4] = 10
print( arr1, arr2, id( arr1 ), id( arr2 ) )     # Compare values of arr1[2],arr2[2],arr2[4],arr[1]
print()

# 2] Deep Copy - Both array are independent for each array always. like if I change one of the array's element than other array will not change.

from numpy import *

arr1 = array( [1, 8, 6, 4, 0, 3, 9] )
arr2 = arr1.copy()
arr1[2] = 7
arr2[4] = 10
print( arr1, arr2, id( arr1 ), id( arr2 ) )     # Compare values of arr1[2],arr2[2],arr2[4],arr[1]
print()