add = lambda a, b: a+b

def divide(a, b):
    if b == 0:
        raise ValueError('Cannot divide by Zero')
    return a/b