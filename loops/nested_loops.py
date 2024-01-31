# step 1: kitni lines h -->  i
# kitne stars h --> j

'''
Q1.
*****
*****
*****
*****
*****
'''
for i in range(1, 6):   #5 lines h
    for j in range(1,6):  #5 stars h
        print("*", end=" ")
    print()

'''
Q2.
12345
12345
12345
12345
12345
'''

for i in range(1, 6):
    for j in range(1, 6):
        print(j, end=" ")
    print()

'''
Q3.
54321
54321
54321
54321
54321
'''

for i in range(1, 6):
    for j in range(5,0,-1):
        print(j, end=" ")
    print()

'''
Q.
11111
22222
33333
44444
55555
'''

for i in range(1,6):
    for j in range(1,6):
        print(i, end=" ")
    print()

'''
Q5.
55555
44444
33333
22222
11111
'''

for i in range(5,0,-1):
    for j in range(1,6):
        print(i, end="")
    print()