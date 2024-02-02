
# default args
def add(a, b=0):
    return a + b


# multiple args
def multiply(*args):
    # *args gives a tuple
    prod = 1
    for arg in args:
        prod *= arg

# kwargs
def add1(**kwargs):
    # **kwargs returns a dictionary
    for k,v in kwargs:
        print(f"{k} --> {v}")

# combination
def combo(a, b, *args):
    pass
