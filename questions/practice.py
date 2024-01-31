# for i in range(1, 6):
#     for j in range(1, i+1):
#         print(i, end=" ")
#     print()

# for i in range(1, 6):
#     for j in range(5, i-1, -1):
#         print(i, end=" ")
#     print()

# rows = 5
# for i in range(1, rows + 1):
#     for j in range(1, i+1):
#         print(j, end=" ")
#     print()

"""
55555
4444
333
22
1

"""

# for i in range(5, 0, -1):
#     for j in range(1, i+1):
#         print(i, end=" ")
#     print()

"""
55555
5555
555
55
5
"""

# for i in range(5, 0, -1):
#     for j in range(i):
#         print(5, end=" ")
#     print()

"""
1
21
321
4321
54321
"""

# for i in range(1, 6):
#     for j in range(i, 0, -1):
#         print(j, end=" ")
#     print()

"""
012345
01234
0123
012
01
"""

# for i in range(6, 1, -1):
#     for j in range(i):
#         print(j, end=" ")
#     print()

"""
1
234
56789
"""
currentNumber = 1
stop = 2
rows = 3 # Rows you want in your pattern
for i in range(rows):
    for j in range(1, stop):
        print(currentNumber, end=' ')
        currentNumber += 1
    print("")
    stop += 2