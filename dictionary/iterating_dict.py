student = {
    "name": "aman",
    "class": 10,
    "roll_no": 1,
    "name": "goku",
    1: 2,
}

for k in student.keys():
    print(k)

for v in student.values():
    print(v)

# k will print keys and v will print values
for k,v in student.items():
    # [(), (), ()]
    print(f"{k} --> {v}")