def describe_pet(animal_type, name):
    print(f"I have a {animal_type} named {name}.") 


# Positional arguments
# Positional arguments are passed in the order defined in the function.
describe_pet("Hamster", "Chew-bark-a") # I have a Hamster named Chew-bark-a.
# Result: I have a Hamster named Chew-bark-a.

# Keyword arguments
# Keyword arguments are passed as key-value pair.
describe_pet(animal_type="Hamster", name="Chew-bark-a") # I have a Hamster named Chew-bark-a.
# Result: I have a Hamster named Chew-bark-a.

# Positional-Only Arguments
def my_function(name, /):
    print(f"Hello, {name}!") 
my_function("Alice")  # Hello, Alice!
# my_function(name="Alice")  # This will raise a TypeError because 'name' is a positional-only argument.

# Keyword-Only Arguments
def my_function(*, name):
    print(f"Hello, {name}!")
my_function(name="Alice")  # Hello, Alice!
# my_function("Alice")  # This will raise a TypeError because 'name' is a keyword-only argument.

# Combining Positional-Only and Keyword-Only
# Arguments before / are positional-only, and arguments after * are keyword-only:
def my_function(positional_arg, /, *, keyword_arg):
    print(f"Positional: {positional_arg}, Keyword: {keyword_arg}") 
my_function("Positional Value", keyword_arg="Keyword Value")  # Positional: Positional Value, Keyword: Keyword Value



# Variable-Length Arguments
# names will be a tuble, and arg2 will be a keyword argument.
# The *names allows for any number of positional arguments to be passed, and they will be collected into a tuple named names.
# Arguments passed after the *names must be specified as keyword arguments.
def my_function(greeting, *names, arg2):
    print(greeting) # Hello
    print(names) # ('Alice', 'Bob')
    print(arg2) # This is a keyword argument

my_function("Hello", "Alice", "Bob", arg2="This is a keyword argument")

def sum1(*numbers):
    return sum(numbers)
print(sum1(1, 2, 3, 4)) # 10
print(sum1(2,5)) # 7

# we can also pass a list of numbers to the function using the unpacking operator *
print(sum1(*[1,2,3,4])) # 10


# Arbitary Keyword Arguments
# The **kwargs allows for any number of keyword arguments to be passed, and they will be collected into a dictionary named kwargs.
# Name will be a positional argument, and age and city will be keyword arguments collected in the kwargs dictionary.
def my_function(name,**kwargs):
    print(f"Name: {name}") # Name: Alice
    print(kwargs) # {'age': 30, 'city': 'New York'}
my_function("Alice", age=30, city="New York")

# Unpacking Arguments
def my_function(a, b, c):
  return a + b + c
numbers = [1, 2, 3]
result = my_function(*numbers) # Same as: my_function(1, 2, 3)
print(result)

def my_function(fname, lname):
  print("Hello", fname, lname)

person = {"fname": "Emil", "lname": "Refsnes"}
my_function(**person) # Same as: my_function(fname="Emil", lname="Refsnes")