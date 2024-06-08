import math
def cal_f1_score(tp,fp,fn):
    #  Check input is int
    if  all(isinstance(i, (int|float)) for i in [tp, fp, fn]) == False:
        print("input is not is a number")
        return

    # Check input = 0
    if  all(i > 0 for i in [tp, fp, fn]) == False:
        print("input is zero")
        return
    
    precision = tp/(tp + fp)
    recall = tp/(tp + fn)
    f1_score = 2* (precision*recall)/(precision+recall)
    
    return f1_score