import numpy as np 
import random as rand
import math 


def new_pos(n): # defining new position of the node 
	return rand.randrange(0,n*100,1) / (n * 100)



n = 5000
    	
a = [] 
node = []
k = 0.38
l = 42.2

# scale = 42.2 
# shape = 0.38


for i in range(0,n):
	r = []
	r.append(float(i/n))
	r.append(float(math.ceil(np.random.weibull(k,1)*l)))
	a.append(r)
	if i % 500 == 0 : 
		print(i)


#print(a)
counter = []
mx = []
mim = []
avg = []
coun = 0
var = 4

for k in range(10000): #Timesteps 
	x = 0
	
	for i in range(0,n):
		
		#print(a[i][1])
		a[i][1] -= 1

		if a[i][1] == 0.0 :

			new = new_pos(n)
			while new in a:
			
				new = new_pos(n)

			a[i][0] = new #position of new node 
			a[i][1] = float(math.ceil(np.random.weibull(k,1)*l)) # TTL of node using Weibull 

	count = []
	while (var*(x+1)*math.log(n))/n <= 1 : #Calculating the number of nodes in a group 
		coun = 0
		for i in range(0,n):
			
			if a[i][0] <= (var*(x+1)*math.log(n))/n and a[i][0] >= (var*x*math.log(n))/n : # grouping 
				coun += 1 

		count.append(int(coun))

		x += 1

	mx.append(int(max(count)))
	mim.append(int(min(count)))
	avg.append(int(np.average(count)))


print('Maximum',mx)
print()

print('Minimum',mim)
print()

print('Average',avg)


