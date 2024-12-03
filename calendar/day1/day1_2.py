import numpy as np

data = np.loadtxt('input.txt')

list1, list2 = data[:, 0], data[:, 1]

result = 0
for data1 in list1:
    sim = 0
    for data2 in list2:
        if(data1 == data2):
            sim += 1
    result += sim * data1

print(result)
