import check_number
def calc_ae(y,y_hat):
    if (isinstance(y,(int|float)) == False or isinstance(y_hat,(int|float)) == False):
        print('input is not a number')
    ae = abs(y - y_hat)
    return ae

def calc_se(y,y_hat):
    if (isinstance(y,(int|float)) == False or isinstance(y_hat,(int|float)) == False):
        print('input is not a number')
    se = (y - y_hat)**2
    return se