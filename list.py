# List is mutable.
# 'Mutable' means after assigning value to the variable, we can change it as per our need.
# To create list we use ' [] ' - Square Brackets.


# Sample Program - 1    :   To create list

number = [1, 3, 24, 0, 35, 46, 83, 6, 19]       # Integer type
names = ['maks', 'khush', 'wh']                 # String type
values = [25, 'maks', 9.8, 's']                 # Combination of different datatype
print( number )
print( values )
print( type( number ), type( values ) )
print()

# Sample Program - 2    :   list of list (combining list in list)

mix = [number, names, values]
print( mix, type( mix ) )
print()

# Sample Program - 3    :   Operations on list

number.insert( 2, 77 )              # insert(index,value)
print( number )
number.remove( 3 )                  # remove(value) - it will delete element by values
print( number )
number.pop( 1 )                     # pop(index) - it will delete element by index number
print( number )
number.pop()                        # pop() - by defalt it will delete last element of the list as "LIFO"
print( number )
del number[2:5]                     # del - to delete multiple values togather...   del list_name[starting_point : end_point]   where, end_point excluded
print( number )
number.extend( [135, 146, 145] )
print( number )                     # to add multiple elements at a time
print()
number.sort()                       # to sort the list
print(number)

# Sample Program - 4    :   update value of the list

print( "Value available at index 2 : ", number[2] )
number[2] = 5
print( "New value available at index 2 : ", number[2] )