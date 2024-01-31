marks = [40, 23, 65, 75, 85, 20, 56, 33, 27, 19, 54]

# print in reverse order

for i in range(len(marks) - 1, -1, -1):  # 5 to 0
    print(marks[i], end=" ")

# --------------------------------------------

# print all even numbers in the list

for i in marks:
    if i%2 == 0:
        print(i, end=" ")

# -------------------------------------
# print numbers at even index

for i in range(0, len(marks)):
    if i%2 == 0:
        print(marks[i])

# -----------------------
# print sum of all elements
sum = 0
for i in marks:
    sum += i
print(sum)

# ----------------------
# count even numbers in the list
even_nums = 0

for i in marks:
    if i%2 ==0:
        even_nums += 1
print(even_nums)

# --------------------------
# sum of numbers divisible by 3 or 4

sum = 0
for i in marks:
    if i%3 == 0 or i%4 == 0:
        sum += i
print(sum)

# ---------------
# print the largest number
largest = 0
for i in marks:
    if i > largest:
        largest = i
print(largest)

# seprate even and odd
even = []
odd = []

for num in marks:
    if num%2 == 0:
        even.append(num)
    else:
        odd.append(num)