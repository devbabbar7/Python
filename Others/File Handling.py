# Reading a file
file = open('a.txt', 'r')
# Only the first one of the below code snippets will print because the pointer moved from start to end
print(file.read()) # reads entire file
print(file.readline()) # reads first line of the file as pointer keeps moving to next line
print(file.readlines()) # converts all lines of the file into a list
file.tell()    # Current pointer position
file.seek(0)   # Move pointer to beginning
file.close() # close is always required. It prevents memory leak.
# Open files using with instead because it automatically closes the file if we forget
# In real life application, we always prefer to use with while opening any files
with open('a.txt', 'r') as file:
    print(file.read())



# Write/Appending a file
file = open('a.txt', 'w') # This will overwrite the file 
# file = open('a.txt', 'a') # This will add to the file without overwriting existing changes
file.writelines(['Hello\n', 'Dev\n', 'Babbar\n']) # Adding \n is necessary, it doesn't do it by itself
file.write('Hello, Dev') # This will append to the previous write and writelines function calls
file.close()


# To delete a file
import os
if os.path.exists("a.txt"): # to prevent crashes
    os.remove("a.txt")

# Mode  Meaning
# 'r'   read
# 'w'   write (overwrite)
# 'a'   append
# 'r+'  read + write
# 'w+'  write + read (overwrite)
# 'a+'  append + read
# 'rb'  read binary
# 'wb'  write binary
