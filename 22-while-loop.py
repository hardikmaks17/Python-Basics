# Main three parts for while loop : 1) Initialization
#                                   2) Condition
#                                   3) Increment/Decrement


# Sample Program - 1 : Increament


i = 1                                   # Initialization
while i<=5:                             # Condition
    print("Maks")
    i+=1                                # Increment
print("\n")


# Sample Program - 2 : Decreament


i = 5
while i>=1:
    print("WH")
    i-=1                                # Decrement
print("\n")


# Sample Program - 3 : Print number of times as well as with it


i = 1
while i<=5:
    print("Maks ",i)
    i+=1
print("\n")


# Sample Program - 4 : Print in same line all outputs,  ==>>        end=""


i = 1
j = 1
while i <= 5:
    print("We",end="")
    while j <= 4:
        print("Maks",end="")
        j+=1
    i+=1
print("\n")


# Sample Program - 4 : Get output as below pattern

# WeMaksMaksMaksMaks
# WeMaksMaksMaksMaks
# WeMaksMaksMaksMaks
# WeMaksMaksMaksMaks
# WeMaksMaksMaksMaks


i=1
while i<=5:
    print("We",end=" ")
    j=1
    while j<=4:
        print("Maks",end=" ")
        j+=1
    i+=1
    print()
