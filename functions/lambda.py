# writes a function in a short way
add_nums = lambda a, b: a + b

add_nums(10, 20)

# take a number and make a list from 0 to n
num = int(input("Enter a number --> "))

make_list = lambda n: [nums for nums in range(n+1)]
print(make_list(num))

# take a number return True if even else false
# else block is compulsory
check_even = lambda n: print("even") if n%2 == 0 else print("False")


