a = 15

def change():
    # local variable 
    # it is not changing the a declared above
    a = 30
    print(a)

# changing global var in a function
def change_global():
    global a
    a = 30
    # now the value of a is changed
    