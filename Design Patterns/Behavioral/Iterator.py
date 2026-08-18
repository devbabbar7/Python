class Countdown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        current = self.start
        while current > 0:
            yield current
            current -= 1

a = Countdown(3)

for i in a:
    print(i)

for i in a:
    print(i, end = ' ') 

# Output:
# 3
# 2
# 1
# 3 2 1