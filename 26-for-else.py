# For Else loop in PYTHON. It is not available in other programming language.

nums = [10,16,18,21,26]
for i in nums:
    if(i%5==0):
        print('divisible : ',i)
        break
else:
    print('not found')
