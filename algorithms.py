

def fibonacci(n):
    if (n == 0):
        return 0

    if(n == 1):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

def fast_fibonacci(n):
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