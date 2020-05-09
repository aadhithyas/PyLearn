# functions:
# allows reuse of code
# DRY - Don't Repeat Yourselves


# def: keyword to define a function
# hello_func(): name of the function:
# hello_func(): name of the function:
# () to get the parameters
def hello_func():
    print("Hello World!, Welcome to Python function")


# function returning some value
def hello_func_return():
    welcome = "Hello World! Welcome to PYTHON FUNCTION"
    return welcome


# main program
if __name__ == "__main__":
    # call the function by its name
    hello_func()

    # get a value returned from a function
    greeting = hello_func_return()
    print(greeting)
