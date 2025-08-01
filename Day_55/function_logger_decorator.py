# TODO: Create the logging_decorator() function 👇
def logging_decorator(function):
    def wrapper(*args):
        # Print the name of the function
        print(f"You called {function.__name__}", end = "")
        # Print the arguments given
        print("(", end="")
        i = 0
        while i < len(args):
            if len(args) - 1 == i:
                print(args[i], end="")
            else:
                print(args[i], end=", ")
            i += 1
        print(")")
        output = function(*args)
        print(f"It returned: {output}")
        return output
    return wrapper


# TODO: Use the decorator 👇
@logging_decorator
def a_function(*args):
    return sum(args)
    

print(a_function(4,5,6))