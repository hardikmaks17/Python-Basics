# Break , Continue & Pass are the keywords!

# 1) Break Keyword :

# Sample Program - 1    this program is not correct for inputs ( x > 11) need some improvements
av = 10                 # av = available
x = int( input( "How many Candies you want?\n" ) )
i = 1
while i <= x:
    if i <= av:
        print( "Candy", i )
    else:
        print( "Out of stock!" )
    i += 1
print( '\n' )

# Sample Program - 2   above program using 'Break keyword'
av = 10
x = int( input( "How many Candies you want?\n" ) )
i = 1
while i <= x:
    if i > av:
        print( "Out of stock!" )
        break
    print( "Candy", i )
    i += 1
print( '\n' )

# 2) Continue Keyword :

# Sample Program - 1    print values which are not divisible by 3
for i in range(1,101):
    if i%3==0:                  # not divisible by 3        skip values like - 3,6,9,12...
#   if i%3==0 or i%5==0:        # not divisible by 3 or 5   skip values like - 3,5,6,9,10...
#   if i%3==0 and i%5==0:       # not divisible by 3 and 5  skip values like - 15,30,...
        continue
    print(i)
print('bye')
print( '\n' )

# 3) Pass Keyword :

# Sample Program - 1    print values which are even
for i in range(1,101):
    if(i%2!=0):
        pass
    else:
        print(i)