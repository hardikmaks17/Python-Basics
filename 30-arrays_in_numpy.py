# Ways of Creating Arrays in Numpy
# There are 6 ways to create array in numpy : 1] array()    2] linspace()   3] logspace()   4] arrange()    5] zeros()  6] ones

# Way - 1   :   array()

from numpy import *
arr = array([1, 5, 8.5, 3, 4])                      # you can also describe type of the array like this - array([1, 5, 8.5, 3, 4],type)     where, type = int,float...
print("Way - 1 : array() --",arr)                   # you can verify in the output that integer values are converted into float automatically because of 8.5 ! (as we know all values should be in same type)
print(arr.dtype)                                    # variablename.dtype : to get type of the array
print()

# Way - 2   :   linspace()

from numpy import *
arr = linspace(1,16,16)                             # stop point included so it will go grom 1 to 16.
print("Way - 2 : linspace() --",arr)
print(arr.dtype)
print()

# Way - 3   :   logspace()

from numpy import *
arr = logspace(1, 4,3)
print("Way - 3 : logspace() --",arr)
print("first value in normal form :" '%.2f' %arr[0])
print("last value in normal form  :" '%.2f' %arr[2])
print(arr.dtype)
print()

# Way - 4   :   arange()

from numpy import *
arr = arange(1,15,2)
print("Way - 4 : arange() --",arr)
print(arr.dtype)
print()

# Way - 5   :   zeros()

from numpy import *
arr = zeros(5)                                      # By default it will create float values as zeros array
print('Float values :',arr)
print(arr.dtype)
arr = zeros(5,int)                                  # Specify 'int' to create integer zeros array
print('Integer values :',arr)
print(arr.dtype)
print()

# Way - 6   :   ones()

from numpy import *
arr = ones(5)                                       # By default it will create float values as ones array
print('Float values :',arr)
print(arr.dtype)
arr = ones(5,int)                                   # Specify 'int' to create integer ones array
print('Integer values :',arr)
print(arr.dtype)
print()
