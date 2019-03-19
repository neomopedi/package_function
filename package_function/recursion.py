def sum_array(array):
    return(sum(array))


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def factorial(n):
    if n <1:   # base case
        return 1
    else:
        returnNumber = n * factorial( n - 1 )  # recursive call
    print(str(n) + '! = ' + str(returnNumber))
    return returnNumber


def reverse(word):
    return word[::-1]
    
