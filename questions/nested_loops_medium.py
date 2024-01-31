'''
Q1.
1
12
123
1234
12345
'''

for i in range(1,6):    #5 lines h
    for j in range(1,i+1):  #kitni bar print krna h? jitna i h utna
        print(j, end=" ")
    print()

'''
Q2.
1
22
333
4444
55555
'''

for i in range(1, 6):
    for j in range(1, i+1):
        print(i, end=" ")
    print()

'''
Q3.
1
21
321
4321
54321
'''

for i in range(1,6):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()

'''
Q.
54321
4321
321
21
1
'''

for i in range(5, 0, -1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()

'''
*****
****
***
**
*
'''

for i in range(5, 0, -1):
    for j in range(1, i+1):
        print("*", end=" ")
    print()