# There is two types of argument : 1] Formal Argument   2] Actual Argument

# 1] Formal Argument - Whatever parameter/argument we define in function while defining funtion is called "Formal Argument".

# 2] Actual Argument - After calling function whatever we give value the funtion is called "Actuak Argument".
#    => There is 4 types of actual argument :
#       1) Position
#       2) Keyword
#       3) Default
#       4) Variable Length


# Sample Program - 1    :   Types of Function Argument

def add(x,y):                           # here (x,y) is - Formal Argument

    c = x + y
    print("Addition :",c)

add(5,6)                                # here (x,y) is - Actual Argument
print()


# Sample Program - 2    :   Types of Actual Argument


# Program - 1   :   Position Argument

def person(name,age):
    print("Name of the Person :",name)
    print("Age of the Person  :",age)

person('Maks',21)
print()
person(21,'Maks')
print()
# Above, compare line 30 & 32 position of arguments are needed true, otherwise it can give wrong output.
# So this is "Position Argument".


# Program - 2   :   Keyword Argument

def person(name,age):
    print("Name of the Person :",name)
    print("Age of the Person  :",age)

# If we don't know position of the parameter , we can write directly name of the parameter and assign the value...  See below...
person(age=21,name='Maks')                          # 'age' & 'name' are called as "Keyword"
print()


# Program - 3   :   Default Argument

def person(name,age=18):                            # "By Default" age = 18 is defined.. So if user dosen't give value of age than function will consider it as 18; otherwise it will take value of age as given by the user.
    print( "Name of the Person :", name )
    print( "Age of the Person  :", age )

person('Khush')                                     # Default age is 18.
print()
person('Maks',21)                                   # Age value entered
print()


# Program - 4   :   Variable Length Argument  -  This argument is useful when we are not sure about how many parameter we need.

# See below example where we can add for undefined times of values.

def sum(*b):

    c = 0
    for i in b:
        c = c + i
    print("Summation of",i,"inputed numbers :",c)

sum(1,2,3,4,5)
print()


# Sample Program - 3    :   Keyworded Variable Length Argument

def person(name, *data):                                    # ' * ' - single star

    print(name)
    print(data)

person('Maks',28,'Baroda',8999903113)                      # Problem - Here output is generated but we don't know what is 28,'Baroda' is hometown or work place...
person('Maks', age=28, city='Baroda', mob=8999903113)      # Problem - 'unexpected keyword argument' or no output


def perso(name, **data):                                   # ' * ' - single star

    print(name)
    print(data)

perso('Maks', age=28, city='Baroda', mob=8999903113)