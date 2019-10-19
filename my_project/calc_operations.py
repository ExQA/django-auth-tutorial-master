import math

def add(a, b):
    return a + b

def minus(a, b):
    return a - b

def umn(a, b):
    return a * b

def dell(a, b):
    return a / b

def expt(a, b):
    if b == 0:
        return 1
    return a*expt(a, b-1)

def sin(a, b):
    return math.sin(a)
def cos(a, b):
    return math.cos(a)

calc_object = {
    '+': add,
    '-': minus,
    '*': umn,
    '/': dell,
    '^': expt,
    'sin': sin,
    'cos': cos,
}


calc_object_non_auth = {
    '+': add,
    '-': minus,
    '*': umn,
    '/': dell,
    '^': expt
}



