# Q6
def my_function ( data , max_value , min_value) :
    result = []
    for i in data :
        if  i < min_value:
            result.append(min_value)
        elif i > max_value:
            result.append(max_value)
        else :
            result.append(i)
        # print(i,max_value,min_value,result)
    return result
my_list = [5 , 2 , 5 , 0 , 1]
max_value = 1
min_value = 0
assert my_function (max_value = max_value , min_value = min_value , data = my_list ) == [1 , 1 , 1 , 0 , 1]
my_list = [10,2,5,0,1]
max_value = 2
min_value = 1
print ( my_function (max_value = max_value , min_value = min_value , data = my_list ) )

# Q7

def my_function (x = list , y = list ):
    z = x.extend(y)
    return x

# Q8
def min_function ( n ) :
    min_value = n[0]
    
    # Iterate through the list starting from the second element
    for value in n[1:]:
        if value < min_value:
            min_value = value
    
    return min_value

# factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
# Q14
def my_function(x):
    # Reverse the string and return it
    return x[::-1]

# Q15
def function_helper(x):
    # If x > 0 = T else N
    if x > 0:
        return 'T'
    else:
        return 'N'

def my_function(data):
    res = [function_helper(x) for x in data]
    return res

# Q16 

def function_helper(x, data):
    for i in data:
        if x == i:
            return 0
    return 1

def my_function(data):
    res = []
    for i in data:
        if function_helper(i, res):
            res.append(i)
    return res