import matplotlib.pyplot as plt
year=[int(x) for x in (input()).split()]
salary=[int(x) for x in input().split()]
if len(year) == len(salary):
 plt.plot(year,salary)
 print(plt.show())
else:
    print("The graph is not structured")