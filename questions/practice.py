"""
traingle sidha h --> i wala loop +ve
triangle ulta h --> i wala loop -ve

pattern sidha h --> j loop +ve chalega
pattern ulta h --> j loop -ve chalega

pattern has same numbers --> print(i) e.g 1 22 333 4444
pattern has sequential numbers -> print(j) eg. 1 12 123 1234
"""

"""
1
22
333
4444
55555
"""

# for i in range(1, 6):
#     for j in range(1, i + 1):
#         print(i, end=" ")
#     print()

"""
11111
2222
333
44
5
"""
# num = 1
# for i in range(5, 0, -1):
#     for j in range(i, 0, -1):
#         print(num, end=" ")
#     print()
#     num += 1

"""
1
12
123
1234
12345
"""
# for i in range(1, 6):
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
# for i in range(5,0,-1):
#     for j in range(1 , i+1):
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
# for i in range(5, 0, -1):
#     for j in range(0, i+1):
#         print(j, end=" ")
#     print()

"""
1
234
56789
"""
# 2n- 1

# end_num = 1

# for i in range(1, 4):
#     for j in range(1, 2*i):
#         print(end_num, end=" ")
#         end_num += 1
#     print()


"""
1

3 2

6 5 4

10 9 8 7
"""