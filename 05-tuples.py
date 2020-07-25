# Tuples is immutable.
# 'Immutable' means after assigning value to the variable, we can't change it as per our need.
# To create list we use ' () ' - Open Brackets.
# Iteration is faster in tuples than list.  So if value is fixed that always prefer tuples for program.


# Sample Program - 1    :   To create tuples

i = (1,5,7,9,-4,16,31,13,17)
print("Integer in tuples       :",i,type(i))
s = ('maks','khush','wh')
print("String in tuples        :",s,type(s))
m = (5,-83,'maks','wh')
print("Mixed values in tuples  :",m,type(m))
print()

# Sample Program - 2    :   fetching values from the tuples

print("Value of index number 0 is :",i[0])
print("Value of index number 1 is :",s[1])
print("Value of index number 3 is :",m[3])

print(i[2 : 4])                                                       # it will exclude end_point which is index number 4
print(i[  : 4])                                                       # it wil give values of index number 0 to 3
print(i[3 :  ])                                                       # it wil give values of index number 3 to to last
print("Value of index number -1 is :",i[-1])                          # negative index value starts from "right to left"... So -1 will give last value
