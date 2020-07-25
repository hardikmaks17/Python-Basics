num = int(input("Enter a number : "))
if num > 1:
    for i in range(2,num):
        if num % i == 0 :
           print(num,"is Not a Prime Number.")
           print(i,"times",num//i,"is",num,".")
           break
    else:
        print(num,"is a Prime Number.")
else:
    print(num,"is not a Prime Number.")