def fibonacci(n):
    """
    Return the nth value in the fibonacci series
    """
    if type(n) == int:
        first_number = 0
        second_number = 1
        if n == 0:
            return first_number
        elif n == 1:
            return second_number
        else:
            return fibonacci(n-1) + fibonacci(n-2)
    else:
        return("Put an intger")
print(fibonacci("ss"))

def lucas(n):
    """
    Returns the nth value in the lucas numbers
    """
    if type(n) == int:
        first_number = 2
        second_number = 1
        if n == 0:
            return first_number
        elif n == 1:
            return second_number
        else:
            return lucas(n-1) + lucas(n-2)
    else:
        return("Put an intger")
# print(lucas(7))

def sum_series(n, o_1=0 , o_2=1):
    """
    The required parameter (n) will determine which element in the series to print. The two optional parameters (o_1,o_2) will have default values of 0 and 1 and will determine the first two values for the series to be produced.
    """
    if type(n) == int and type(o_1) == int and type(o_2) == int :
        first_number = o_1
        second_number = o_2
        if n == 0:
            return first_number
        elif n == 1:
            return second_number
        else:
            return sum_series(n-1,first_number,second_number) + sum_series(n-2,first_number,second_number)
    else:
        return("Put an intger")
# print(sum_series(7,2,1))

# f(5) = f(4) + f(3)
# f(4) = f(3) + f (2)
# f(3) = f(2) + f(1)  
# f(2) = f(1) + f(0) 
# 
# 
# f(5) = f(1) + f(0) + f(1) + f(1) + f(0) + f(1) + f(0) + f(1) 





  


