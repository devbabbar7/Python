# Generator functions can pause and resume their execution and they return a generator object which is an iterator 
# Generators are memory-efficient because they generate values on-the-fly instead of storing everything in memory.
def count_up_to(n):
    count = 1
    while count <= n:
        # when yield is called, the function's state is saved and the value of count is returned to the caller. 
        # When the next value is requested, the function resumes execution right after the yield statement, with all its variables and state intact.
        yield count
        count += 1

gen = count_up_to(5)

print(next(gen))  # Output: 1
print(next(gen))  # Output: 2
print(next(gen))  # Output: 3
print(next(gen))  # Output: 4
print(next(gen))  # Output: 5
print(next(gen))  # This will raise StopIteration since the generator is exhausted