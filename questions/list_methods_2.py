# *** NEVER CHANGE IN THE GIVEN LIST i.e. MAKE A NEW LIST ***

my_list = [45, 33, 45, "aman", 78, "aman", 52.3]

# # Remove duplicates
filtered_list = []

for element in my_list:
    if element not in filtered_list:
        filtered_list.append(element)
print(filtered_list)

# # ask a number. if exists, print its position
num = int(input("Enter a number --> "))
if num in my_list:
    print(my_list.index(num))
else:
    print(-1)

# # average of numbers in the list
new_list = [44, 55, 66, 25, 14]
summation = 0
n = len(my_list)

for num in new_list:
    summation += num
average = summation / n
print(average)

# element with highest occurance
l2 = [44, 14, 56, 44, 12, 14, 44]

highest_count = 0
highest_occuring_num = 0
for num in l2:
    count = l2.count(num)
    if count > highest_count:
        highest_count = count
        highest_occuring_num = num
print(highest_occuring_num)

# 2 lists and print common elements
l1 = [2, 10, 15, 36, 75]
l2 = [15, 63, 36, 174]
common = []

for num in l1:
    if num in l2 and num not in common:
        common.append(num)
print(common)

# 2nd largest element in a list
l3 = [45, 74, 112, 53, 56, 20]
largest = 0
second_largest = 0

for num in l3:
    if num > largest:
        second_largest = largest
        largest = num
print(second_largest)

# prinitng prime numbers
# prime numbers have 2 factors i.e. check if factors are more than 2 through a loop from 1 to that number
l4 = [2, 10, 7, 55, 11, 3]
primes = []

for num in l4:
    factors = 0
    for n in range(1, num+1):
        if num%n == 0:
            factors += 1
    if factors == 2:
        primes.append(num)
print(primes)