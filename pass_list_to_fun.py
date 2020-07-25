# Pass 'List' to a Function.
# In other words we will give input as list in user defined function.

list = [1,5,-7,15,178,32]

def count(list):

    even = 0
    odd = 0

    for i in list:
        if i%2==0:
            even+=1
        else:
            odd+=1

    return even,odd

list = [1,5,-7,15,178,32]
even,odd = count(list)

#print("Even :",even)
#print("Odd  :",odd)

print("Even : {} and Odd : {}".format(even,odd))