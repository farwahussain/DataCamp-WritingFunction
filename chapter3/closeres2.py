#task 1: Show that you still get the original message even if you redefine my_special_function() to only print "hello".
def my_special_function():
  print('You are running my_special_function()')
  
def get_new_func(func):
  def call_func():
    func()
  return call_func

new_func = get_new_func(my_special_function)

# Redefine my_special_function() to just print "hello"
def my_special_function():
  print("hello")

new_func()
print("------------------Task2--------------------")
#Task 2: Show that even if you delete my_special_function(), you can still call new_func() without any problems.
# Delete my_special_function()
del my_special_function

new_func()

print("------------------Task3---------------------")
#Show that you still get the original message even if you overwrite my_special_function() with the new function.

my_special_function = get_new_func(my_special_function)

my_special_function()