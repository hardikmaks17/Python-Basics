# if,elif,else statements in python.
# Indent matters in this... So be carefull always... Hence always use "tab" for spaceing.
# After these statements whatever coming below this at same space will be consider that it is coming in this part...
# If indent is not same than it is not under that part.


# Sample Programme - 1  :   To check number is ODD / EVEN


x = int(input('Enter any number : '))
r = x % 2
if r==0:
    print("Even number")
else:
    print("Odd number")
print('Bye')


# Sample Programme - 2  :   To find greatest among three numbers


x = int(input("Enter first number  : "))
y = int(input("Enter second number : "))
z = int(input("Enter third number  : "))

if x>y and y>z:
    print('x is the greatest')
elif y>x and y>z:
    print('y is the greatest')
elif z>x and z>y:
    print('z is the greatest')
else:
    print("Equal number inserted")
