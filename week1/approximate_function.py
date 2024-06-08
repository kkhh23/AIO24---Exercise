import factorial as f
def sin(x,n):
    if (isinstance(x,(int|float)) == False or isinstance(n,(int|float)) == False):
        print('input is not a number')
    result = 0
    for i in range(n):
        result += ((-1)**i * x**(2*i + 1)) / f.factorial(2*i + 1)
    return result

def cos(x,n):
    if (isinstance(x,(int|float)) == False or isinstance(n,(int|float)) == False):
        print('input is not a number')    
    result = 0
    for i in range(n):
        result += ((-1)**i * x**(2*i)) / f.factorial(2*i)
    return result

def sinh(x,n):
    if (isinstance(x,(int|float)) == False or isinstance(n,(int|float)) == False):
        print('input is not a number')    
    result = 0
    for i in range(n):
        result += x**(2*i + 1) / f.factorial(2*i + 1)
    return result

def cosh(x,n):
    if (isinstance(x,(int|float)) == False or isinstance(n,(int|float)) == False):
        print('input is not a number')    
    result = 0
    for i in range(n):
        result += x**(2*i) / f.factorial(2*i)
    return result