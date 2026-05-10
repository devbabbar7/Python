from pathlib import Path

# 1. PATH SETUP & CREATION
p = Path(r'C:\Users\User\Documents\CS PROGRAMMING\Python\DailyProgress')
p2 = p / 'NewFolder' / 'SubFolder' # create a new path by joining the original path with a new folder name
# parents=True: creates all missing parents (like mkdir -p)
# exist_ok=True: ignores error if folder already exists
p2.mkdir(parents=True, exist_ok=True)

# 2. PATH MANIPULATION
p2.rmdir() # remove the subfolder
p2.parent.rmdir() # remove the parent folder

source = p / 'oldfile.txt'
source.touch() # create an empty file if it does not exist, if it already exists, it will update the last modified time of the file
destination = p / 'newfile.txt'
# Below replace will move the file to the new location and rename it to newfile.txt, if the destination file already exists, it will be overwritten.
source.replace(destination)

# 3. RENAMING FILES
destination.rename(p / 'updatedfile.txt') # rename the file.
destination.with_stem = 'description' # change the stem of the file to 'description' (the name of the file without the suffix)
destination.with_suffix('.md') # change the suffix of the file to .md (markdown file)
destination.with_name('readme.md') # change the name of the file to readme.md (the name of the file with the suffix)

# check if its an absolute path or not
print(p.is_absolute()) 

for subdir in p.iterdir():
    if subdir.is_dir(): # if it is a directory, print the whole path
        print(subdir)
    else:
        # stem is the name of the file without the suffix
        print(subdir.name, subdir.suffix, subdir.stem) # DailyProgress.py .py DailyProgress
        print(subdir.parent) # directory of the file (original path without the file name)

# Searching for files
# glob is basically a regex pattern but only with * and ? wildcards. * matches any number of characters (including none) and ? matches any single character. You can also use [abc] to match any of the characters a, b, or c, and [!abc] to match any character except a, b, or c.
# rglob is the same as glob but it also searches in subdirectories. It is basically a recursive version of glob. It is equivalent to glob('**/*.py') which means it will search for all .py files in the directory and subdirectories.
files = p.glob('*.py') # get all .py files in the directory (not including subdirectories) in a generator object
files = p.rglob('*.py', case_sensitive=False) # get all .py files in the directory and subdirectories in a generator object
files = p.glob('*.*') # get all files in the directory (not including subdirectories) in a generator object
files = p.glob('*vscode*') # get all files in the directory (not including subdirectories) that have 'vscode' in their name in a generator object

for file in files:
    print(file.name)

# Writing to a file
with (p / 'output.txt').open('w') as file:
    file.write("Hello, GFG!")

p2 = Path(__file__)
print(p2.absolute()) # get the absolute path of the current file
p2 = p2.parent
print(p2.absolute()) # get the directory of the current file
# You can use p2.resolve() or p2.absolute() to get the absolute path of the current file or directory.
print(Path.cwd()) # get the current working directory
