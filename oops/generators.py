from random import randint

# -------------------

# give something one by one
# 1. yield

def give_random_numbers():
    yield randint(1, 50)
    yield randint(1, 50)
    yield randint(1, 50)
    yield randint(1, 50)

for n in give_random_numbers():
    print(n)

# next() 
# moves to next yield

next(give_random_numbers())
next(give_random_numbers())
next(give_random_numbers())

# ----------------
# 2. raise
# to raise an exception/error
print(5+5)
raise IndexError()