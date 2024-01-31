# Key value pairs
# keys are always unique while value can repeat
# {key: value}

student = {"name": "aman", "class": 10, "roll_no": 1}

# if you use same keys, the last key will be used
student = {
    "name": "aman",
    "class": 10,
    "roll_no": 1,
    "name": "goku",
    1: 2,
}  # name will now be goku and not aman

# accessing keys
print(student["name"])
student.get("name")

# print(student["abvhdj"])        #KeyError

k = input("Enter a key --> ")

if student.get(k) is not None:
    print(student[k])
else:
    print("Does not exist")

# changing value
student["name"] = "goku"
student["xyz"] = "abc"  # add xyz if does not exist or update if extsts

# changing multiple values
# accepts a dictionary
student.update({"marks": 45, "name": "Gohan"})

# deleting 
student.pop("name")
student.pop("jfjhfh")   #KeyError
del student["name"]