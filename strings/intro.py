# strings are iterable
# strings are immutable

a = "aman"
type(a)

# immutable
# a[0] = "m"  #Error

# iteration
for char in a:
    print(char, end="-")

# reverse
for i in range(len(a)-1, -1, -1):
    print(a[i])