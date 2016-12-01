__author__ = "Sriram Jayaraman"

import matplotlib.pyplot as plt
print ("Enter the values of X-axis: ")
year=[int(x) for x in (input()).split()]
print ("Enter the values of Y-axis: ")
salary=[int(x) for x in input().split()]
if len(year) == len(salary):
 plt.plot(year,salary)
 print(plt.show())
else:
    print("The graph is not structured")
