marks = [45, 20, 23, 56, 71, 55]

# FUNCTIONS

sum(marks)  # finding sum
max(marks)  # largest number
min(marks)  # smallest number
len(marks)  # finding length

# METHODS

# 1. add elements
marks.append(200)  # adds to the end
marks.insert(3, 77)  # add on a specific index
marks.insert(500, 77)  # if index doesn't exist, adds at last

# 2. update elements
marks[0] = 72
marks[400] = 10  # error index doesnt exist

# 3. delete elements
marks.pop()  # last element
marks.pop(0)  # element at 0 index
marks.pop(400)  # error

del marks[0]

marks.remove(23)  # remove by value (1st time element)
marks.remove(73)  # error

marks.clear()  # empties the list

# Finding index
marks.index(45)  # 45 ka index (1st time occurance)
marks.index(12456)  # Value Error

# sorting
marks.sort()  # ascending order (doesnt return anything)
marks.sort(reverse=True)  # descending order

# reverse
marks.reverse()

# concatinating 2 lists
new_list = [45, "aman"]
marks.extend(new_list)

# count number of times something is occuring
marks.count(55)

# Copying
# a = b is not good because python stores data in memory and both a and b will point towards same adress therefore if a is changed b will also change
copied_list = marks.copy() # stores at a different address from a

# the adress in the memory where a variable is stored
id(marks) 