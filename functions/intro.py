def add(n1, n2):    #parameters
    return n1 + n2

x = add(5, 7)   #arguments
print(x)

# return
# if a function doesnt return anything, the var will be None
def hello():
    print("Hello")
msg = hello()   # msg = None

# scoping
# vars declared inside a function cant be accessed outside

product = 999
def multiply(a, b):
    product = a *b
    return product
multiply(8, 9)
print(product)  #999 and not a*b

