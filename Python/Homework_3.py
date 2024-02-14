#Just handels printing data
def printData(a):
    local = []
    key = []
    for x in a.keys():
        local.append(len(x))
        key.append(x)

    largest = max(local)
    print(" " * (largest + 2), end="")

    for k in key:
        print(k, end="   ")

    print(" ")
    for key,value in a.items():
        smalls = len(key)
        spaces = largest - smalls + 5
        print(key, end=" ")
        print(" " * spaces, end="")
        for n in range(len(value)):

            if type(value[n]) == float or value[n] >= 10:
                print(value[n], end=" " * (largest - 4))
            elif value[n] > 99:
                print(value[n], end=" " * (largest))
            else:
                print(value[n], end=" " * (largest - 3))

        print("")


#2 parts. 1st get all permutations. Then sort lexicographically
def lexicoPermu(n):
    og = []
    permutate = [[]]
    i = 1
    while i <= n:
        og.append(i)
        i += 1

    for num in og:
        new = []
        for p in permutate:
            for index in range(len(p) + 1):
                new.append(p[:index] + [num] + p[index:])
        permutate = new

#The sort below is a SelectionSort taken form GeeksforGeeks
#Link: https://www.geeksforgeeks.org/selection-sort/

    for array in range(len(permutate)):
        minimum = array
        for j in range(minimum + 1, len(permutate)):
            if permutate[minimum] > permutate[j]:
                minimum = j

        permutate[array], permutate[minimum] = permutate[minimum], permutate[array]

    return permutate

#Question 1
num = int(input("Please Enter a number to find all permutations + sort it: "))
all = lexicoPermu(num)

for z in all:
    print(z)

#Question 2
data = {}
n_index = []
stack = []

cities = int(input("Please enter the number of cities you want to represent: "))

for number in range(cities):
    graph = []
    name = input("Please enter the name of the city: ")
    n_index.append(name)

    print("\nYou will now be adding the values to different cities. You do not need to add the value connecting to your own city.")
    print("If you add any zeros, the first written zeros will be assumed to be the correct weight")
    print("Any attempt to add a weight other than zero will lead it to be overridden with a zero\n")

    # A majority of the code below is created for error handeling

    for n in range(cities - 1):
        value = int(input("Please enter the values to connecting cities: "))
        if value == 0:
            if n == 0:
                stack.append((name, 1))
            else:
                stack.append((name,n))
        graph.append(value)

    graph.insert(number, 0)
    data[name] = graph


#Override different array spots with zero if you place any zero between node. Ex you place zero for a spot
#Then you place try to place 5 in the adjacent spot. The 5 will be overridden and turned to a zero.

for zero in stack:
    curr = stack.pop()
    p = n_index.index(curr[0])
    c = n_index[curr[1]]
    data[c][p] = 0

printData(data)








