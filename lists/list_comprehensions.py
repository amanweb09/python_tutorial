# faster way to make a list
# jo b i ki value for loop main hogi vohi value bahar wale i ki hogi

my_list = [i for i in range(1, 11)]
# [1, 2,...10]

my_list_2 = ["aman" for i in range(1, 21)]
# [aman, aman, aman, ...]

my_list_3 = [i % 2 for i in range(1, 21)]
# [1,0,1,0...]

# conditionals

# case 1: add hamesha kro lekin kya add krna h uske liye if else
# if else before loop
# else part is compulsory
my_list_4 = ["Even" if i % 2 == 0 else "Odd" for i in range(1, 21)]

# case 2: sirf kuch conditions pe hi add kro
# if else after loop
# else part is not added
my_list_5 = [i for i in range(1, 21) if i % 2 == 0]

# ask start and end number for user and make a list of all divisible by 2 and 3
start = int(input("Enter a start number --> "))
end = int(input("Enter an end number --> "))
div_by_3_and_2 = [i for i in range(start, end + 1) if i % 2 == 0 and i % 3 == 0]
print(div_by_3_and_2)