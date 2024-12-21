#write a decorator that will let you tag your functions with an arbitrary list of tags.
from functools import wraps

def tag(*tags):
    # Define a new decorator, named "decorator", to return
    def decorator(func):
         # Ensure the decorated function keeps its metadata
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Call the function being decorated and return the result
            return func(*args, **kwargs)
        wrapper.tags = tags 
        return wrapper
    # Return the new decorator
    return decorator

@tag('Tests', 'This is a tag')
def foo():
    pass

print(foo.tags)