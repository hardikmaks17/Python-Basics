# Note - all columns are depended on rows in every program.


# Sample Program - 1    :       # i=number of columns, j=number of rows

for i in range(4):
    for j in range(4):
        print('# ',end='')
    print()
print('\n')


# Sample Program - 2    :       # i=number of columns, j=number of rows

for i in range(4):
    for j in range(i+1):
        print('# ',end='')
    print()
print('\n')


# Sample Program - 3    :       # i=number of columns, j=number of rows

for i in range(4):
    for j in range(4-i):
        print('# ',end='')
    print()
print('\n')


# Practice Program - 1    :     # i=number of columns, j=number of rows

for i in range(4):
    for j in range(i+1):
        print(j+1,end=' ')
    print()
print('\n')


# Practice Program - 2    :     # i=number of columns, j=number of rows

for i in range(4):
    for j in range(4-i):
        print(j+1,end=' ')
    print()
print('\n')
