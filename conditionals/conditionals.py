
# age = input("Enter your age \n")

# if int(age) > 18:    #colon
#         # 4 spaces or 2 tabs
#         print("Can drive")
# else:   # 4 spaces or 2 tabs
#         print("done")

# FINDING GREATER NUMBER

n1 = int(input("enter number 1 \n"))
n2 = int(input("enter number 2 \n"))

if n1 > n2:
        print(f"{n1} is greater!")
else:
        print(f"{n2} is greater!")

# CHECKING EVEN OR ODD

num = int(input("Enter a number \n"))

if num%2 == 0:
        print("The number is even")
else:
        print("The number is odd")


# CHECK VOWEL OR CONSONANT
char = input("Enter a character \n")

if(char == "a" or char == "e" or char == "i" or char == "o" or char == "u"):
        print("vowel")
else:
        print("consonant")

# ELIF
x = 15

if x > 15:
        print("greater")
elif x <15:
        print("Lesser")
else:
        print("equal")