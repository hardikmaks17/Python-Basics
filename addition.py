#Here you will not get output as you expected, beacuse it is taking input as string by default

x = input("Enter 1st number : ")
print("DataType of x ans is : ",type(x))
y = input("\nEnter 2nd number : ")
print("DataType of y ans is : ",type(y))
z = x + y
print("\nAddition of this two number is : ",z)
print("DataType of final ans is : ",type(z))
print("\n")

#In this program I have converted input to integer so now, it will give answer as we wanted.

x = int(input("Enter 1st number : "))
print("DataType of x ans is : ",type(x))
y = int(input("\nEnter 2nd number : "))
print("DataType of y ans is : ",type(y))
z = x + y
print("\nAddition of this two number is : ",z)
print("DataType of final ans is : ",type(z))