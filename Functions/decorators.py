# Decorators
import time

def time_calculate(func): # Decorator function
    def wrapper():
        start = time.perf_counter()
        func()
        print(f"{func.__name__} took", time.perf_counter() - start)
    return wrapper # decorator function should return a wrapper function ideally as to not execute without calling it

@time_calculate
def func1():
    print("Hello")
    time.sleep(.5)
    print("Updating everything...")
    time.sleep(1.3)
# This calls func1 = time_calculate(func1) instantly

def func2():
    print("Welcome")

if __name__ == "__main__": # To ensure code only runs when a script is executed directly, not when imported
    func1() # eqv: func1 = time_calculate(func1) -> func1 = wrapper()
    func2()
    # Output of above:
    # Hello
    # Updating everything...
    # func1 took 1.800123456 seconds
    # Welcome