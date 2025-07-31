# Decorators
from time import sleep
def delay_decorator(function):
    def wrapper_function():
        #Adding a 2 sec delay which is the additional functionality
        sleep(2)
        # Calling the function
        function()
    
    return wrapper_function

@delay_decorator
def say_hi():
    print("Hi")

say_hi()
