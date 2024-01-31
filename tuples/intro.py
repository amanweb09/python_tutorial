
# tuples are immutable
# tuples are iterable

my_tup = (2, 15, 74, "aman")
type(my_tup)

# accessing position
my_tup[0]

# methods
c = my_tup.count(15)
index = my_tup.index(74)

# iteration
for x in my_tup:
    print(x)

# adding elements
my_list = list(my_tup)
my_list.append(100)
my_tup = tuple(my_list)