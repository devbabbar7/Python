class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last
    @property # This is the getter
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    @fullname.setter
    def fullname(self, name):
        self.first, self.last = name.split()
    @fullname.deleter
    def fullname(self):
        self.first, self.last = None, None
b = Employee('Niharika', 'Sharma')
print(b.fullname) # Niharika Sharma
b.fullname = 'Niharika Babbar'
print(b.fullname) # Niharika Babbar
del b.fullname
print(b.fullname) # None None
