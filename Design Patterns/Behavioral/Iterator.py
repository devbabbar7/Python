class Countdown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        current = self.start
        while current > 0:
            yield current
            current -= 1

class Iterate:
    def __init__(self, list1):
        self.list1 = list1
        self.index = 0

    def __iter__(self):
        while len(self.list1) > self.index:
            yield self.list1[self.index]
            self.index += 1

class IterateWithoutYield:
    def __init__(self, list1):
        self.list1 = list1
        self.index = 0

    def __iter__(self): # Returning self means class is its own iterator, defining __next__ is now mandatory
        return self

    def __next__(self):
        if self.index < len(self.list1):
            self.index += 1
            return self.list1[self.index - 1]
        else:
            raise StopIteration
        

a = Countdown(3)

for i in a:
    print(i)

# 3
# 2
# 1

for i in a: # It is reusable
    print(i, end = ' ') 
print() # For newline

# 3 2 1

aa = Countdown(3)
iteraa = iter(aa)
print(next(iteraa))
print(next(iteraa))
print(next(iteraa))

# 3
# 2
# 1


for i in Iterate([5,10,15]):
    print(i, end = ' ')
print()

# 5 10 15


b = IterateWithoutYield([10,20,30])
print(b.__next__()) # 10
print(next(b)) # 20
print(b.__next__()) # 30
# print(next(b)) # Stop Iteration error will come