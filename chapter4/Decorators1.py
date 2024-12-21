#Task: write a decorator, print_return_type(), that will print out the type of the variable that gets returned from every call of any function it is decorating.

def print_return_type(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print('{}() Returned type {}'.format(func.__name__, type(result)))
        return result
    return wrapper

@print_return_type
def foo(value):
    return value

print(foo(42))
print(foo([1, 2, 3]))
print(foo({'a': 42}))