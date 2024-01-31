name = "aman khanna"

# title case (My Name Is Aman)
cc = name.title()

# uppercase
uc = name.upper()
is_uc = name.isupper()  # check if uppercase

# lowercase
lc = name.lower()
is_lc = name.islower()

# lower ones to upper and upper ones to lower
swap = name.swapcase()

# check is only alphabets are there
is_alphabets = name.isalpha()

# check is only alphabets and digits are there
is_alphnum = name.isalnum()

# check if only digits
is_digit = name.isdigit()

# check for space
is_space = name.isspace()

user_input = "1245"
if user_input.is_digit():
    print(int(user_input))

# find method
# returns -1 for non existent and returns the index for others
name.find("a")

# starts with
name.startswith("a")
name.endswith("x")

# replace
new = name.replace("a", "e")

# remove spaces from end
x = "    hello    "
x.strip()

y ="****aman****"
y.strip("*")