def md_nre_single_sample2 (y , y_hat , n , p ) :
    if isinstance(y,(int|float)) == True or isinstance(y_hat,(int|float)) == True or isinstance(n,(int|float)) == True or isinstance(p,(int|float)) == True: 
        y_root = y ** (1/ n )
        y_hat_root = y_hat ** (1/ n )
        difference = y_root / y_hat_root
        loss = difference ** p
        return loss
    else: print('input is not a number')