# BREAK is to stop the loop

for i in range(1, 101):
    print(i)
    if i==10:
        break

# sum numbers till the sum is less than 1000
sum = 0
for i in range(1, 101):
    if sum > 1000:
        break
    sum += i

print(sum)