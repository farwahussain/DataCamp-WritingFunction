#Task: create one decorator, html(), that can take any pair of opening and closing tags.

from functools import wraps

def html(opentag, closetag):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            msg = func(*args, **kwargs)
            return '{}{}{}'.format(opentag, msg, closetag)
        return wrapper
    return decorator

#Make hello() return bolded text
@html('<b>', '</b>')
def hello(name):
    return 'Hello, {}!'.format(name)

print(hello('Alice'))

#Make goodbye() return ilatic text
@html('<i>', '</i>')
def goodbye(name):
    return 'Goodbye, {}!'.format(name)

print(goodbye('Alice'))

# Wrap the result of hello_goodbye() in <div> and </div>
@html('<div>', '</div>')
def hello_goodbye(name):
    return '\n{}\n{}\n'.format(hello(name), goodbye(name))

print(hello_goodbye('Alice'))