# If we want to pass multiple data that too with the help of keyword than we have to use - Keyworded Variable Length Argument (KVLA)


# Sample Program - 1    :   Keyworded Variable Length Argument (VLA)


# Problem___ we can't print keyword here in output


def person(name, *data):                                    # ' * ' - single star : Here we can't use undefined keyword during VLA.

    print(name)
    print(data)

person('Maks',28,'Baroda',8999903113)                       # Problem - Here output is generated but we don't know what is 28,'Baroda' is hometown or work place...
#person('Maks', age=28, city='Baroda', mob=8999903113)      # Problem - 'unexpected keyword argument'
print()


# Solution___ Now we can print keyword in output using Keyworded Variable Length Argument (KVLA)


def p(n, **d):                                               # ' ** ' - double star : here we can use undefined keyword name while VLA.

    #print(n,end=' ')
    #print(d)
    # Above two line will print output in tuples

    # To print output individually we can use 'for loop' like using below code

    print('name',n)
    for i,j in d.items():

        print(i,j)

p('Maks', age=28, city='Baroda', mob=8999903113)

