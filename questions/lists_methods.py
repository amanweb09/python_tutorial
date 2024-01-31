# ask user length then ask numbers and make a list
# length = int(input("Hi! My name is Jarvis.\n Enter the length ---> "))
# my_list = []

# for i in range(1, length + 1):
#     ele = input("Enter an element = ")
#     my_list.append(ele)

# print(f"Here's your list --> {my_list}")

# ask user a number and a new number. replace old number with new number
# l1 = [44, 55, 66, 77, 88, 44, 99]
# old_num = int(input(f"Choose a number from this list \n{l1}: "))
# new_num = int(input("Enter a new number: "))

# for i in range(0, len(l1)):
#     if l1[i] == old_num:
#         l1[i] = new_num
# print(l1)

# remove all even numbers
l1 = [44, 55, 66, 77, 88, 44, 99]
filtered_l1 = []

for i in l1:
    if i % 2 != 0:
        filtered_l1.append(i)
print(filtered_l1)
