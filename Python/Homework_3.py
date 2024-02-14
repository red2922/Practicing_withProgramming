def inputValidator(cities):
    local_data = {}
    local_array = []

    for i in range(cities):
        name = input("Please enter your city name: ")
        local_array.append(name)

    for c in local_array:
        values = []

        for x in range(len(local_array)):
            if c != local_array[x]:
                value = int(input(f"Please enter an value for {c} to {local_array[x]}: "))
                values.append(value)
            else:
                continue

        values.insert(local_array.index(c),0)
        local_data[c] = values

    return local_data


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
                print(value[n], end=" " * (largest - 3))
            elif value[n] > 99:
                print(value[n], end=" " * (largest))
            else:
                print(value[n], end=" " * (largest - 2))

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

cities = int(input("Please enter the number of cities you want to represent: "))

data = inputValidator(cities)

printData(data)








