import math
def calc_sig (x):
    if isinstance(x,(int|float)) == False:
        print('input is not a number')
    else :result = 1 / 1 + math.exp(-x)
    return result