import check_number
import math
def activation_function(x,activation_name):
    # check x is number
    if  check_number.is_number(x) == False:
        print("input is not a number")
        return
    # activation function
    match activation_name:
        case 'sigmoid':
            return 1 / (1 + math.exp(-x))
        case 'relu':
            return max(0, x)
        case 'elu':
            return x if x > 0 else 0.01 * (math.exp(x)-1)