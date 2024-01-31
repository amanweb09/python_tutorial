# ask a string and tell how many alphabets
# value = input("Enter a word --> ")
# print(f"{value} has {len(value)} characters")

# ask a string and tell only how many alphabets are there
# value = input("Enter any string --> ")

# count = 0
# for ch in value:
#     if ch.isalpha():
#         count += 1
# print(count)

# ask a string and tell how many upper and lowercase are there
value = input("Enter a word --> ")
uppers = 0
lowers = 0

for ch in value:
    if ch.isupper():
        uppers += 1
    elif ch.islower():
        lowers += 1
print(f"The words {value} has {uppers} uppercase chars and {lowers} lowercase chars")