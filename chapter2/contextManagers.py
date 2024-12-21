#Task: Write a custom context manager
#Add a decorator that will make timer() a context manager
import contextlib
import time

@contextlib.contextmanager
def timer():
    """ Time the execution of the code block
    yiels: 
      None
    """
    start = time.time()
    
    #Sends back the control to context block
    yield
    end = time.time()
    print("Elapsed: {:.2f}s".format(end - start))
    
with timer():
    print("This shoild take approximately 0.25 seconds")
    time.sleep(0.25)