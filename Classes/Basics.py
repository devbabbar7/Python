class Employee: #parent class
    raise_amt = 1.04
    num_of_emps = 0

    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@deventerprises.com'
        self.salary = None
        Employee.num_of_emps += 1
        self.__id = first[0] + last[0] + str(Employee.num_of_emps)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def getId(self):
        return self.__id

    def setSalary(self,salary):
        try:
            self.salary = salary
        except:
            print('Error occured.')

    def apply_raise(self):
        self.salary = self.salary * self.raise_amt

    @classmethod
    def raise_amtClass(cls, val):
        cls.raise_amt = val
    def raise_amtInst(self, val): 
        self.raise_amt = val

    @staticmethod
    def pi():
        from math import pi
        return pi

    def Employee(self, a):
        return "Hi, " + a
    
class Developer(Employee):
    def __init__(self, first, last, prog_lang):
        super().__init__(first, last)
        # Employee.__init__(self, first, last) # Same as above
        self.prog_lang = prog_lang
    
a = Developer('Dev', 'Babbar', 'Python') #instance
b = Employee('Niharika', 'Sharma')
print(a.fullname) # Dev Babbar
a.setSalary(100000)
print(a.getId()) # DB1 (Since it's a protected variable, it can't be called direclty and has to be retrieved using a get method)

Employee.raise_amtClass(1.06) # Since all instances and subclass inherit Employee's raise_amt
print(Employee.raise_amt) #1.06
print(Developer.raise_amt) #1.06
print(a.raise_amt) #1.06
print(b.raise_amt) #1.06

# cls instance in this method considers cls as Developer 
# Updates value for Developer subclass not the parent Employee class
a.raise_amtClass(1.04) 
print(Employee.raise_amt) #1.06
print(Developer.raise_amt) #1.04
print(a.raise_amt) # 1.04
print(b.raise_amt) #1.06


# Notice how it didn't update value for Developer and instance a. but when we called Employee.raise_amtClass(1.06) it updated for all.
# Before we called the previous a.raise_amtClass(1.04), Developer was inheriting raise_amt from Employee.
# After, when we called a.raise_amtClass(1.04), it set a raise_amt value for the Developer class so now Developer class has it's own raise_amt rather than using the inherited copy from Employee.
# Now if you call Employee.raise_amtClass(1.06) again, it will not update raise_amt for instance a and Developer subclass.
b.raise_amtClass(1.08)
print(Employee.raise_amt) #1.08
print(Developer.raise_amt) #1.04
print(a.raise_amt) # 1.04
print(b.raise_amt) #1.08


# Only updated for the instance
# Before It was inherting raise_amt from it's Class Developer but now it has it's own raise_amt which will work seperately and not be updated if we update Developer's raise_amt
a.raise_amtInst(1.1)
print(Employee.raise_amt) #1.08
print(Developer.raise_amt) #1.04
print(a.raise_amt) #1.1
print(b.raise_amt) #1.08


print(Employee.num_of_emps) #2

print(a.Employee('Dev')) # Hi, Dev

# you have to specify the instance as part of self in function argument for a non-staticmethod and non-classmethod
print(Employee.Employee(a, 'Dev')) # Hi, Dev


print(a.pi()) #3.14...
print(Employee.pi()) #3.14...
