# How to get gretest among three numbers.


# Way - 1 : using nested if

a = int(input('Enter first number  : '))
b = int(input('Enter second number : '))
c = int(input('Enter third number  : '))

if a>b:
    if a>c:
        print('a is the greatest.')
    else:
        print( 'c is the greatest.' )
elif b>a:
    if b>c:
        print( 'b is the greatest.' )
    else:
        print( 'c is the greatest.' )
else:
    #print( 'c is the greatest.' )
    print( 'Same number inserted.' )
