# To print values of the list we can use below program.


# Sample Program : 1

x = ['Maks', 65, 2.5]                   # list
print( x )
print('\n')

# Que - What if I want to print these all values individually ?
# Ans. Using for loop we can do it.


# Sample Program : 2

x = ["Maks",65,2.5]                     #list

for i in x:
    print(i)
print('\n')


# Sample Program : 3

x = 'HardikMaks'
for i in x:
    print(i)
print('\n')


# Sample Program : 4

for i in 'Maks':                        #instead of taking variable we can directly write collection(Maks) like this,,, compare it with above ex.
    print(i)
print('\n')


# Sample Program : 5

for i in range(1,11):                   #(starting point, ending point, iteration) we can use it as per our requirement like - (ending point only) / (starting point, ending point)
    print(i)
print('\n')


# Sample Program : 6

for i in range(11,21,2):                #(starting point, ending point, iteration)
    print(i)
print('\n')


# Sample Program : 7    -   to use range() in reverse order

for i in range(20,10,-1):               # Note - (20,10) _ it will not give any output we should write iteration part _ we cant write range(20,10)
    print(i)
print('\n')


# Sample Program : 8    -   only print values which are divisible by 10

for i in range(1,101):
    if(i%10==0):
        print(i)
