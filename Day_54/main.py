import time
current_time = time.time()
print(current_time) # seconds since Jan 1st, 1970 

# Write your code below 👇

def speed_calc_decorator(function):
  # Making a wrapper funciton
    def wrapper_function():
        time_1 = time.time()
        function()
        time_2 = time.time()
        total_time = time_2 - time_1
        return total_time
    return wrapper_function

@speed_calc_decorator
def fast_function():
  for i in range(1000000):
    i * i
        
@speed_calc_decorator
def slow_function():
  for i in range(10000000):
    i * i
    
print(f"fast_function run speed: {fast_function()}s")
print(f"slow_function run speed: {slow_function()}s")
