def func_a(x):
    return x

def func_b(x):
    return x
    
def func_c(x):
    return x

def func_default(x):
    return x

#you can create a dictionary of functions
func_dict={
    'cond_a': func_a,
    'cond_b': func_b,
    'cond_c': func_c
}

cond='cond_a'
func_dict.get(cond, func_default)() #this will call func_default when the key is not found

#a shorter way, but this is too slow
#should store the dictionary in a variable
def operations(operator, x, y):
    return {
        'add': lambda: x+y,
        'sub': lambda: x-y,
        'mul': lambda: x*y,
        'div': lambda: x/y
    }.get(operator, lambda:None)()