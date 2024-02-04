# we can define functions in modules


def circle(radius: float) -> float:
    return 3.14 * (radius**2)


def rectangle(length: float, breadth: float) -> float:
    return length * breadth

# only execute if we run this file and not when we import this file as module
if __name__ == "__main__":
    rectangle(20, 5)