# decorated are predefined codes that we can run 

def my_decorator(func):
    # function -> decorated k bad wala function will be autoinjected here
    def inner_function():
        # this will run before function is called
        print("i am a decorator :)")
        func()

    return inner_function

# my_decorator function will be auto run before print_me runs
@my_decorator
def print_me() -> None:
    print("You are printed")

print_me()