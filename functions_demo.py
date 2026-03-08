"""
// C# method with optional param
public string FormatName(string first, string last = "Sharma") {
  return $"{first} {last}";
}
// C# Action / Func
Func<int, int> square = x => x * x;
"""

def format_name(first:str, last:str = "Sharma"):
    return f"{first} {last}"


# lambda replaces func in c#
square = lambda x: x * x

"""
public void Log(params string[] messages) {
    foreach (var msg in messages) Console.WriteLine(msg);
}
Log("Server started", "DB connected", "Ready"); // pass as many as you want
"""

# *args is equivalent to params[] in C#

def log(*messages: str, prefix: str = "INFO") -> None:
    for message in messages:
        print(f"[{prefix}]: {message}")

log("Server sarted", "DB connected", "Ready", prefix="BODY")

# **kwargs -> There's no equivalent for this in C#. 
# Use it when you need to send a dictionary as argument in a function

def configure(**settings):
    for key, value in settings.items():
        print(f"{key} : {value}")

configure(host = "localhost", port = 8000)

# Using both together

def my_decorator(func):
    def wrapper(*args, **kwargs):   # accept ANYTHING the original function accepts
        print("Before")
        result = func(*args, **kwargs)  # pass it all through unchanged
        print("After")
        return result
    return wrapper

# Order always goes: normal params → *args → **kwargs

# A decorator is a function that wraps another function to 
# add behaviour before and/or after it runs. Without 
# touching the original function's code.

# Let's build  decorator.

# Step 1 - Create a function over which you need a decorator

def get_users():
    return ["Konpal", "Harshit"]

# Let's say you want to log every time you need to call it.
# So you create a wrapper first.

# def wrapper():
#     print("Calling function")
#     result = func()
#     print("Function call ended")

# Issue in this -> You don't have access to the function here.... 
# and you don't return anything here
# So you create a decorator over the wrapper function

def logger(func):
    def wrapper():
        print("Calling function")
        result = func()
        print("Function call ended")
        return result
    return wrapper

# How to use it now? update get_users as follows:

get_users = logger(get_users)

get_users()

# another implementation

@logger
def get_users1():
    return ["Ravi", "Priya"]

get_users1()

# but this only works on a single func... we want it to run for all func types

def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print("Done")
        return result
    return wrapper

# Now we can use this simple logger functionlity on any type of function

@logger
def sum(a:int, b: int):
    return a+b

@logger
def print_names(names:list):
    for name in names:
        print(name)

sum(2,2)
print_names(["Konpal", "Harshit"])