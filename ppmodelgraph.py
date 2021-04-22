import matplotlib.pyplot as plt

def Diff(li1, li2): 
    li_dif = [i for i in li1 + li2 if i not in li1 or i not in li2] 
    return li_dif 

x = [1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,16382]

n2_avg =  [1.29E-06,    1.29E-06,	1.35E-06,	1.61E-06,	1.62E-06,	1.65E-06,	1.71E-06,	2.10E-06,	2.58E-06,	3.56E-06,	5.61E-06,	1.03E-05,	1.79E-05,	2.63E-05,	5.06E-05]
n2_max =  [1.39E-06,	1.40E-06,	1.48E-06,	1.79E-06,	1.81E-06,	1.88E-06,	1.94E-06,	2.34E-06,	2.99E-06,	4.03E-06,	6.17E-06,	1.15E-05,	1.97E-05,	2.72E-05,	5.07E-05]
n2_min =  [9.25E-07,	8.99E-07,	8.61E-07,	9.37E-07,	9.18E-07,	7.98E-07,	8.38E-07,	1.15E-06,	1.44E-06,	2.24E-06,	3.56E-06,	6.11E-06,	1.15E-05,	2.29E-05,	5.05E-05]

#y = [n2_max - n2_min for n2_max, n2_min in zip(len(n2_avg))]
y = (Diff(n2_max, n2_min))
plt.plot(x,n2_avg)

plt.errorbar(x,n2_avg, yerr = y)
