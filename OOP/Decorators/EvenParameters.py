def even_parameters(func):
    def wrapper(*args):
        if all([isinstance(x,int)and x%2==0 for x in args]):
            result=func(*args)
            return result
        else:
            return f"Please use only even numbers!"
    return wrapper

@even_parameters
def add(a, b):
    return a + b

print(add(2, 4))
print(add("Peter", 1))