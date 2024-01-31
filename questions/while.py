# ask a number from a user and print 1 to that number
n = int(input("Enter a number ---> "))
count = 1

while count <= n:
    print(count)
    count += 1

# ask a number from a user and print number to 1
n = int(input("Enter a number ---> "))

while n >= 1:
    print(n)
    n -= 1

# Sum of all numbers from 1 to 10
sum = 0
n = 10

while n >= 1:
    sum += n
    n -= 1
print(sum)

# numbers divisible by 7 from 1-100
n = 1
while n <= 100:
    if n%7 == 0:
        print(n)
    n += 1

# sum numbers divisible by 4 from 20 to 50
sum = 0
n = 20
while n <= 50:
    if n%4 == 0:
        sum += n
    n += 1
print(sum)