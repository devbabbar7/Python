class Employee:
    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.email = first.lower() + '.' + last.lower() + '@deventerprises.com'
        self.salary = salary
    
    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def __str__(self): # used for endpoint user
        return 'Employee {}, email: {}'.format(self.fullname, self.email)
    
    def __repr__(self): # used by developer
        return 'Employee {}, email: {} Salary: {}'.format(self.fullname, self.email, self.salary)
    
    def __add__(self, other):
        return self.salary + other.salary
    
    def __len__(self):
        return len(self.first) + len(self.last)
    
    def __gt__(self, other):
        # lt = less than
        # gt = greater than
        # le = less than equal to
        # ge = greater than equal to
        # eq = equal to
        # ne = not equal to
        return self.salary > other.salary


a = Employee('Dev', 'Babbar', 500000)
b = Employee('Niharika', 'Sharma',75000)
print(a) # Employee Dev Babbar, email: dev.babbar@deventerprises.com
print(repr(a)) # Employee Dev Babbar, email: dev.babbar@deventerprises.com Salary: 500000
print(a + b) # 575000
print(len(a)) # 9 -> Dev(3) + Babbar(6)
print(a > b) # True
