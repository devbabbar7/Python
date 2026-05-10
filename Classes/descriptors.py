from typing import Any, Self
# A non-data descriptor example is a class with only __get__.
# Functions are also non-data descriptors.

class NonDataDescriptor:
    def __get__(self, instance : object | None, owner: type[Any]):
        return 'from non-data'
    
# A data descriptor example is a class with both __get__ and __set__.
# It will not update it if called from an object. 
# @Property is an example of a data descriptor. It will not update if age is a property and you call obj.age = 20
class DataDescriptor:
    # self is Example.data (the instance), instance is Ex, owner is Example
    def __get__(self, instance : object | None, owner: type[Any]): 
        return 'from data'
    
    def __set__(self, instance, value):
        pass

class ProtectedMethod:
    def __init__(self, func):
        self.func = func
    def __get__(self, instance, owner):
        # Bind the function to the instance (standard method behavior)
        return self.func.__get__(instance, owner)
    def __set__(self, instance, value):
        # This makes it a DATA DESCRIPTOR
        raise AttributeError("You cannot overwrite this method!")

class Example:
    non_data = NonDataDescriptor()
    data = DataDescriptor()
    def __init__(self):
        self.non_data = "instance value" # Since it's a non-data descriptor, the value of the variable will update.
        self.data = "instance value" # Will not update the value of data variable because it is using a data descriptor.
    
    @ProtectedMethod
    def sum1(self, a, b):
        return a + b


if __name__ == '__main__':
    Ex = Example()
    print(Ex.non_data) # instance value
    print(Ex.data) # from data
    # Because sum1 is a non-data descriptor we can update the function itself from outside without @ProtectedMethod but with @ProtectedMethod, it will not allow.
    Ex.sum1 = lambda a, b, c: a + b + c
    print(Ex.sum1(5,5,5)) # 15