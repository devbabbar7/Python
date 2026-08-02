import copy

class SelfReferencingEntity:
    def __init__(self):
        self.parent = None

    def set_parent(self, parent):
        self.parent = parent

class SomeComponent:
    def __init__(self, some_int, some_list_of_objects, some_circular_ref):
        self.some_int = some_int
        self.some_list_of_objects = some_list_of_objects
        self.some_circular_ref = some_circular_ref

    # This creates a shallow copy, meaning adding change to any of the objects will reflect in both objects.
    def __copy__(self): 
        some_list_of_objects = copy.copy(self.some_list_of_objects)
        some_circular_ref = copy.copy(self.some_circular_ref)
        new = self.__class__(self.some_int, some_list_of_objects, some_circular_ref)
        new.__dict__.update(self.__dict__)
        return new

    # This creates an independent copy
    def __deepcopy__(self, memo=None):
        if memo is None:
            memo = {}

        some_list_of_objects = copy.deepcopy(self.some_list_of_objects, memo)
        some_circular_ref = copy.deepcopy(self.some_circular_ref, memo)

        new = self.__class__(self.some_int, some_list_of_objects, some_circular_ref)
        new.__dict__ = copy.deepcopy(self.__dict__, memo)
        return new


if __name__ == "__main__":

    list_of_objects = [1, {1, 2, 3}, [1, 2, 3]]
    circular_ref = SelfReferencingEntity()
    component = SomeComponent(23, list_of_objects, circular_ref)
    circular_ref.set_parent(component)

    # Adding anything to any of the variables of any object will change them in both objects.
    shallow_copied_component = copy.copy(component)

    deep_copied_component = copy.deepcopy(component)

    a = id(deep_copied_component.some_circular_ref.parent)
    b = id(deep_copied_component.some_circular_ref.parent.some_circular_ref.parent)
    aa = id(component.some_circular_ref.parent)
    bb = id(component.some_circular_ref.parent.some_circular_ref.parent)
    print(a == aa) # False, proving that original and cloned objects are different
    print(a == b) # True, proving that no infinite circular path
    print(aa == bb) # True, proving that no infinite circular path