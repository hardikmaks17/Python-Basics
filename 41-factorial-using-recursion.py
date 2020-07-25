# Finding factorial using recursion.

def fact(n):
    if (n == 0):
        return 1

    return n * fact( n - 1 )

result = fact( n=int( input( "Enter a number : " ) ) )
print( "Factorial of given number :", result )
