

def fibonacci(n):
    if (n == 0):
        return 0

    if(n == 1):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

#Idea is to create a dynamically programmed fibonacci function
def fast_fibonacci(n): #need to create a way to check if it is already inside of the aray or not
    local_aray = []
    if (n == 0):
        return local_aray[0]

    if(n == 1):
        return local_aray[1]

    if(local_aray[n - 2] not in local_aray):
        return fast_fibonacci(n - 2)

    if(local_aray[n - 1] in local_aray):
        return fast_fibonacci(n - 1)

    local_aray[n] = local_aray[n - 1] + local_aray[n - 2]
    return local_aray[n]

def geekforgeeksolutionFib(n):
    fibArray = [0, 1]
    if n < 0:
        print("Incorrect input")
    elif n <= len(fibArray):
        return fibArray[n - 1]
    else:
        temp_fib = fibonacci(n - 1) + fibonacci(n - 2)
        fibArray.append(temp_fib)
        return temp_fib
