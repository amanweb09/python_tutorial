# reverse a string through slicing
def reverse_string(str1):
    return str1[::-1]


# count number of uppercase and lowercase in a string
def count_case(str1):
    cases = {"uppercase": 0, "lowercase": 0}

    for ch in str1:
        if ch.isupper():
            cases["uppercase"] += 1
        elif ch.islower():
            cases["lowercase"] += 1
    return cases


# remove duplicates
def remove_dupli(list1):
    uniques = []

    for ch in list1:
        if ch not in uniques:
            uniques.append(ch)
    return uniques


# check if a number is prime
def check_prime(number):
    factors = 0
    for i in range(1, number + 1):
        if number % i == 0:
            factors += 1
    if factors > 2:
        return False
    else:
        return True


# take a start and end number and print primes

# print words with even length
def even_length(sentence):
    words = sentence.split()
    
    evens = [w for w in words if len(w)%2 == 0]
    return evens

print(even_length("He is not a good boy"))