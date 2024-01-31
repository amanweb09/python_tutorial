# ask a number from a user and print 1 to that number
n = int(input("Enter a number ---> "))

for i in range(1, n+1):
    print(i)

# ask a number from a user and print number to 1
n = int(input("Enter a number ---> "))

for i in range(n, 0, -1):
    print(i)

# Sum of all numbers from 1 to 10
sum = 0
for i in range(1,11):
    sum += i
print(sum)

# numbers divisible by 7 from 1-100
for i in range(1, 101):
    if i%7 == 0:
        print(i)

# sum numbers divisible by 4 from 20 to 50
for i in range(20,50):
    if i%4 == 0:
        print(i)