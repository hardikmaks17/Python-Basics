# Sample Program - 1    :   Getting input from the user

from array import *
arr = array('i',[])                                             # [] - it states : EMPTY ARRAY

n = int(input("Enter size of the array : "))
for i in range(n):
    x = int(input("Enter the next value : "))
    arr.append(x)

print(arr)
print()

# Sample Program - 2   :   Searching index value of the number  # Note it is using above code's array

# Way - 1 : By using for loop

val1 = int(input("Enter a number for search : "))
k=0
for e in arr:
    if e == val1:
        print(k)
        break
    k+=1
else:
    print("Not Found!")

# Way - 2 : By using in built funtion of PYTHON

val2 = int(input("Enter a number for search : "))
print(arr.index(val2))