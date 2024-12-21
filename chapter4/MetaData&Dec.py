#how to preserve docstrings and other metadata when writing decorators.
#Decorate print_sum() with the add_hello() decorator, then print its docstring 

from functools import wraps

def add_hello(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """Print 'hello' and then call the decorated function."""
        print("Hello!")
        return func(*args, **kwargs)
    return wrapper

@add_hello
def print_sum(a, b):
    """Add two numbers and print their sums"""
    print(a + b)
    
print_sum(10, 20)

#Define the docstring
print(print_sum.__doc__)