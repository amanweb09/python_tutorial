"""
    Lists are arrays
    lists = []
    Any datatype can be stores
"""

marks = [54, 55, 60, 52, 40]
l1 = ["aman", 2, 24.5, True]

# finding length
length = len(marks)


# finding the type
print(type(marks))


# finding element at a particular position

    # 1. positive (left to right)
p1 = marks[0]
p2 = marks[1]

    # 2. negative (right to left i.e. ulta start krna)
p_last = marks[-1]


# out of range error --> accessing position that does not exist eg. marks[100]
