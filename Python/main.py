from algorithms import fibonacci as fib
from algorithms import fast_fibonacci as ff
from algorithms import geekforgeeksolutionFib as gf
from algorithms import pascalsRecur as pr
from algorithms import test
from algorithms import idk
from algorithms import printData as testing

"""n = int(input("Please enter a number to calculate the fibonacci: "))
print(fib(n))
print(gf(n))"""


test_data = {"Highschool":[0,0,.5,9,18,2],
             "Middleschool":[0,0,.5,9,18,2],
             "ValleyHigh":[.5,.5,0,9,17,2],
             "Naples":[9,9,9,0,26,11],
             "MountHall":[18,18,17,26,0,17],
             "DistinctOffice":[2,2,2,11,17]}

testing(test_data)

d_aray = [[10,20,30,40],[10,25,30,40]]

for i in range(len(d_aray)):
    for n in range(len(d_aray[i])):
        print(str(d_aray[i][n]) + (5 * " "), end="")