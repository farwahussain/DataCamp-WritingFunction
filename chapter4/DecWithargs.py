#Task: Practice different ways of applying the decorator to the function print_sum()

def run_n_time(n):
    """Define and retuen a decorator"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

#Make print_sum() run 10 times with the run_n_times() decorator
@run_n_time(10)
def print_sum(a, b):
    print(a+b)
    
print_sum(3, 5)

#Use run_n_times() to create the run_five_times() decorator
run_five_times = run_n_time(5)

@run_five_times
def print_minus(a, b):
    print(a-b)
    
print_minus(15, 5)

#Modify the print() function to always run 20 times
print = run_n_time(20)(print)

print("What is happening???")