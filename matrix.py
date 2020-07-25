# How to create Matrix.

# Sample Program - 1   :   To create like matrix

from numpy import *

arr = array([
                [1,2,3],
                [4,-7,6]
            ])
print(arr)
print("Type of the matrix element :",arr.dtype)     # .dtype
print("Dimension of the matrix    :",arr.ndim)      # .ndim
print("Number of rows and Column  :",arr.shape)     # .shape - gives : (row,column)
print("Size of the matrix         :",arr.size)      # .size : row*column
print()


# Sample Program - 2   :    Convert m-D array into n-D array


from numpy import *

arr1 = array([
                [-9,14,5,34,8,56],
                [4,-7,6,15,1,4],
            ])
arr2 = arr1.flatten()                           # .flatten - converts n-D to 1-D matrix
print(arr1)
print("1-D of above matrix :",arr2)
print("Dimension of the matrix :",arr2.ndim)
print()

arr3 = arr2.reshape(4,3)                        # .reshape(parts,row,coloumn)
print(arr3)
print("Dimension of the matrix :",arr3.ndim)
print()

arr3 = arr2.reshape(3,2,2)                      # .reshape(____,row,coloumn)    -   (number of sub matrix,rows,column)
print(arr3)
print("Dimension of the matrix :",arr3.ndim)
print()

# Note  - Above all matrix are actually arrays... like 1-D array, 2-D array, 3-D array,...
#       - it output looks like matrix but we can not perform operations on it, which we used to perform on maths
# Below is actual matrix on which we can perform all operations


# Sample Program - 3   :    To crate matrix


m = matrix('1,2,3 ; 4,5,6 ; 7,8,9')
print("Matrix :\n",m)
print()

# Sample Program - 3   :    Operations on matrix

# 1 - Functions
print("Diagonal elements :",diagonal(m))            # diagonal(name)
print("Minimum element :",m.min())                  # name.min()
print("Maximum element :",m.max())                  # name.max()
print()

# 2 - Addition
m1 = matrix('1,2,3 ; 4,5,6 ; 7,8,9')
m2 = matrix('1,7,8 ; 2,8,4 ; 1,3,8')
print("1st matrix :\n",m1,"\n2nd matrix :\n",m2)
m3 = m1 + m2
print("Addition of two matrix :\n",m3)
print()

# 3 - Multiplications
m1 = matrix('1,2,3 ; -3,5,2 ; 5,1,-2')
m2 = matrix('1,3,-4 ; 2,1,-1 ; 1,3,2')
print("1st matrix :\n",m1,"\n2nd matrix :\n",m2)
m3 = m1 * m2                                            # we can do this also - m1 * 2, m1 ** 3
print("Multiplication of two matrix :\n",m3)