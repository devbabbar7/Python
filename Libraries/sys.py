import sys

sys.exit("Age is less") # Exit the program immediately after printing the message

# Print the Python interpreter version being used
print(sys.version) # 3.14.3

# Print the maximum size of integers that can be handled by Python
print(sys.maxsize) # 9223372036854775807

# List app directories in current folder
print(sys.path)

# When read from the command line, the arguments are stored in sys.argv as a list of strings. 
# The first element is the name of the script being executed, and the subsequent elements are the additional arguments passed to the script.
print(sys.argv) # ['test.py', 'arg1', 'arg2']
print(len(sys.argv)) # 3
