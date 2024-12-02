import numpy as np

data = np.loadtxt('input.txt')

list1, list2 = data[:, 0], data[:, 1]

list1.sort()
list2.sort()

result = 0
for data1, data2 in zip(list1, list2):
    result += abs(data1 - data2)

print(result)
