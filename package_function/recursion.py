def sum_array(array):
    return(sum(array))
    '''Return sum of all items in array'''

def fibonacci(n):
 if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    '''Return nth term in fibonacci sequence'''

def factorial(n):
    if n <1:   # base case
        return 1
    else:
        returnNumber = n * factorial( n - 1 )  # recursive call
    print(str(n) + '! = ' + str(returnNumber))
    return returnNumber
       '''Return n!'''

def reverse(word):
    return word[::-1]
    '''Return word in reverse'''
