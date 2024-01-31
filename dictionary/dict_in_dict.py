student = {
    "aman": {
        "physics": 45,
        "maths": 60,
        "hist": 40
    },
    "chintu": {
        "physics": 45,
        "maths": 70,
        "hist": 23
    },
}

aman_maths = student["aman"]["maths"]
print(aman_maths)

for name, subjects in student.items():
    print(subjects["physics"])