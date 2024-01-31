# ARITHMETIC
"""
    +   add
    -   minus
    /   divide --> always a float
    *   multiply
    %   modulus (remainder)
    **  exponent
    //  floor division ---> always an integer


 10/4 = 2.5
 10//4 = 2 (always lower integer as the answer is 2.5)
 -10//4 = -3 (always lower integer as the answer is -2.5)

    =    assignment operator
    +=   x = x + 5
    *=   x = x*5
    x**= x = x*x*x...
"""

# COMPARISON  ---> Boolean
"""
    > , < , <=, >=, ==, !=
"""

# LOGICAL
"""
    and   True if both statements are true
    or    True if one of the statements is true
    not   returns False is the answer is true
"""

chemsitry = 67
physics = 40

print(physics > 33 and chemsitry > 33) #output -> True
print(not physics > 33)  # output -> false

# Membership 
# works in iterables

my_list = [44, 32, 62.5, "aman"]
print(44 in my_list)    #returns True
print(44 not in my_list)    #False because it exists
