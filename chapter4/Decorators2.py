#Task: write a decorator that adds a counter to each function that you decorate.

def counter(func):
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        # Call the function being decorated and return the result
        return func(*args, **kwargs)
    # Set count to 0 to initialize call count for each new decorated function
    wrapper.count = 0
    #return the new decorated function
    return wrapper

@counter
def foo():
    print("Calling foo()")
    
foo()
foo()

print("foo() was called {} times.".format(foo.count))
