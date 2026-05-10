import os 
from datetime import datetime

cwd = os.getcwd() 
print("Current working directory:", cwd) # Current working directory: C:\Users\User\Documents\CS PROGRAMMING\Python

os.chdir('../') # Go back one folder/dir
print("Current working directory:", os.getcwd()) # Current working directory: C:\Users\User\Documents\CS PROGRAMMING

# available folders/dir in the folder you are in
print(os.listdir()) # ['C', 'C++', 'Python']

os.chdir('Python') # Move forward in directory
print("Current working directory:", os.getcwd()) # Current working directory: C:\Users\User\Documents\CS PROGRAMMING\Python


size = os.path.getsize("test.py") # Get file size
print("Size of the file is", size," bytes.")
stats = os.stat("test.py")
print(stats)
print(stats.st_size) # file size in bytes
print(datetime.fromtimestamp(stats.st_ctime)) # created date time
print(datetime.fromtimestamp(stats.st_mtime)) # last modified date time
print(datetime.fromtimestamp(stats.st_atime)) # acess time


if os.path.exists('a.txt'): # Check for path
    os.rename('a.txt', 'demo.txt') # changed file name
else:
    print('File doesn\'t exist')

# Will walk all the paths
for dirpath, dirnames, filenames in os.walk(os.getcwd()):
    print(dirpath) # current path
    print(dirnames) # directories inside dir
    print(filenames) # files in dir

# Returns None if value doesn't exist
print(os.environ.get('MY_VAR')) # None

# Returns Default value if value doesn't exist
print(os.environ.get('MY_VAR', 'Default value')) # Default value

os.environ["MY_VAR"] = "HelloDev"
print(os.environ.get('MY_VAR', 'Default value')) # HelloDev

# Raises KeyError exception if value doesn't exist
print(os.environ['MY_VAR']) # HelloDev

print(os.path.dirname('Class12/b.py')) # Class12
print(os.path.basename('Class12/b.py')) # b.py
print(os.path.isdir('Class12/b.py')) # False
print(os.path.isfile('Class12/b.py')) # True
print(os.path.split('Class12/b.py')) # ('Class12', 'b.py')


print(os.path.abspath(__file__)) # get the absolute path of the current file

path1 = os.path.dirname(os.path.abspath(__file__)) # get the directory of the current file

# Join path1 with new folder name called 'Hello'
new_path = os.path.join(path1, 'Hello')
os.mkdir(new_path) # create a new directory called 'Hello' in the parent directory of the current file
print(new_path) # print the new path of the 'Hello' directory
