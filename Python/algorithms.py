

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


def pascalsRecur(n):
    if n == 0:
        return 1
    return  n *  pascalsRecur(n - 1)

def test(n,k):
    if k == 1: 
        return 1
    return test(n, k - 1) * n

def idk(n,k):
    if n == k or k == 0:
        return 1
    else:
        return idk(n - 1, k -1) + idk(n - 1, k)


def printData(a):
    local = []
    key = []
    for x in a.keys():
        local.append(len(x))
        key.append(x)

    largest = max(local)
    print(" " * largest, end="")

    for k in key:
        print(k, end="   ")

    print(" ")
    for key,value in a.items():
        smalls = len(key)
        spaces = largest - smalls + 5
        print(key, end=" ")
        print(" " * spaces, end="")
        for n in range(len(value)):
            print(value[n], end=" " * (largest - 3))
        print("")

#2 parts. 1st get all permutations. Then sort lexicographically
def lexicoPermutations(n):
    og = []
    permutate = [[]]
    i = 1
    while i <= n:
        og.append(i)
        i += 1

    for num in og:
        new = []
        for perm in permutate:
            for index in range(len(perm) + 1):
                new.append(perm[:index] + [num] + perm[index:])
        permutate = new

    return sorted(permutate)




