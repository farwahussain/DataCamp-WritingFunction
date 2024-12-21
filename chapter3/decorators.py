#Task: Call the function being decorated and pass it the positional arguments *args.Return the new decorated function.

def print_before_and_after(func):
    def wrapper(*args):
        print("Before {}".format(func.__name__))
        func(*args)
        print("After {}".format(func.__name__))
    return wrapper

@print_before_and_after
def multiply(a, b):
    print(a*b)

multiply(5, 10)