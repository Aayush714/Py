import random as rand 
import math
import matplotlib.pyplot as plt
import numpy 

n = 1000
a = []
node = []
count = 0 
c = []
b = []

while n < 1000000:
    for i in range(n):
        node.append(float(rand.random()))
    
    a = [[0] * math.ceil(n/math.log2(n))]*100000
    c = [[n] * math.ceil(n/math.log2(n))] * 100000
    b = [[0] * math.ceil(n/math.log2(n))]*100000

    for i in range(0,n):
        x = node[i]
        interval = math.ceil(((x*n)/math.log2(n)) - 1)
        a[count][interval] = a[count][interval] + 1

    n = n * 2
    # print(a[count])
    # for i in range(5):
    #     print()
    count += 1 
    # print(c)
    b = numpy.subtract(a,b)/math.log2(n)
    plt.scatter(c[count-1],b[count-1], c = 'b')
print(len(c))
print(len(a))

plt.xscale('log')
plt.show()
plt.savefig('Basic.png')

del a,b,c
