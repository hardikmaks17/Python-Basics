# Finding Factorial.


# Way - 1   :   Directly


n = int(input("Enter a number : "))
fact = 1

if n<=0:
    print("Enter valid number!")
else:

    for i in range(1,n+1):
        fact = fact * i

    print(fact)

print()


# Way - 2   :   Using Function


def fact(n):

    if n<=0:
       print("Enter valid number!")
    else:
        f = 1
        for i in range(1,n+1):

            f = f * i

        print(f)
        return f

x = int(input("Enter a number : "))
fact(x)