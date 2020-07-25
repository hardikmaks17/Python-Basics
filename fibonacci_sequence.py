# Fibonacci Sequence

def fib(n):

    a = 0
    b = 1

# Note : You can do this below condition using if-elif-else also...; Here I'm using nested if-else.
    if n <= 0:
        print("Enter valid number!")

    else:

        if n == 1:
            print(a)

        else:
            print( a )
            print( b )

            for i in range(2,n):            # 2 elements(0 and 1) are printed so 0 and 1 are already occupied, now from index 2 start

                c = a + b
                a = b
                b = c
                print(c)

#n = int(input("Enter number : "))
#fib(n)
fib(n=int(input("Enter number : ")))