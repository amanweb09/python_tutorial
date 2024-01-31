"""
q1. 
     *
    **
   ***
  ****
 *****

"""
# pattern right side h i.e. loop ulta nhi h instead left main spaces h
# toh spaces alag solve hongi aur stars alag solve honge

for i in range(1, 6):
    # for spaces
    for j in range(i, 5):  # i=1 toh loop 4 bar chalega, ...
        print(" ", end=" ")

    # for *
    for k in range(1, i + 1):
        print("*", end=" ")

    print()


"""
   *
  ***
 *****
*******
"""
for i in range(1 , 6):
    # for spaces
    for j in range(i, 5):
        print(" ", end=" ")

    # for *
    for k in range(1, 2*i):
        print("*", end=" ")

    print()