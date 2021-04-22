import numpy as np 
import random as rand
import math 


def new_pos(n): # defining new position of the node 
	return rand.randrange(0,n*100,1) / (n * 100)

def shuffle(x,a,n,var):
    for i in range(0,n): # Moving nodes in region to random location in the ring 
        if a[i][0] <= (var*(x+1)*math.log(n))/n and a[i][0] >= (var*x*math.log(n))/n:
            a[i][0] = rand.randrange(0,1)    
    for i in range(1,(var*math.log(n))): #Uniformly locating nodes  
        node = rand.randrange(1,n)
        a[node][0] = var*x*(math.log(n))/n + (i-1)/n
    return a

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
    
    # if i % 10 == 0: 
    #     r.append(0)
    
    # else :
    #     r.append(1)
    a.append(r)

	


#print(a)
counter = []
mx = []
mim = []
avg = []
coun = 0
var = 4
grp_status = []

for t in range(10000): #Timesteps 

	if t < 1000 : # For no attack 
    
        for i in range(0,n):
            
            #print(a[i][1])
            a[i][1] -= 1

            if a[i][1] == 0.0: #TTL for each node, when nodes are dying 

                new = new_pos(n)

                while new in a: 
                    new = new_pos(n)

                a[i][0] = new #position of new node 
                a[i][1] = float(math.ceil(np.random.weibull(k,1)*l)) # TTL of node using Weibull 
        

    else : # For attack 
        for i in range(0,n):
            a[i][1] -= 1
            
            if a[i][2] == 0 : 
                #Defining Adversarial strategy (Discuss)
            
            else :
                # If not adversarial || for good nodes
                if a[i][1] == 0.0: #TTL for each node, when nodes are dying 

                    new = new_pos(n)

                    while new in a: 
                        new = new_pos(n)

                    a[i][0] = new #position of new node 
                    a[i][1] = float(math.ceil(np.random.weibull(k,1)*l)) # TTL of node using Weibull 




    x = 0 
    count = []
    while (var*(x+1)*math.log(n))/n <= 1:  # Calculating the number of nodes in a group
        coun = 0
        for i in range(0, n):

            if a[i][0] <= (var*(x+1)*math.log(n))/n and a[i][0] >= (var*x*math.log(n))/n:  # grouping
                coun += 1

        if coun >= var*(1.2)*math.log(n) and coun <= var*(0.8)*math.log(n) : #Shuffle condition  
            # Need to shuffle 
            a = shuffle(x,a,n,var)


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


