# Swapping of two numbers


# Way - 1   :   Using temporary variable

x = int( input( 'Enter any number : ' ) )
y = int( input( 'Enter any number : ' ) )
print( "\nBefore swapping :", x, y )

temp = x
x = y
y = temp

print( "After swapping  :", x, y )
print()

# Way - 2   :   In PYTHON we can swap directly using it's in-built feature.

a = int( input( 'Enter any number : ' ) )
b = int( input( 'Enter any number : ' ) )
print( "\nBefore swapping :", a, b )

a, b = b, a

print( "After swapping  :", a, b )