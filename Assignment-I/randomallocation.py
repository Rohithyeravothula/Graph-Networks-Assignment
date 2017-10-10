# import start 

import random
import math 

# import end

# definition start

n=10  # number of individuals
t=100 # amount of time stamps
R=100 # resources

# definition end

# abilities 

a=[] #ability
dummy=[]
for i in range(0,n):
	a.append(0)
	dummy.append(random.random())
s=0
for i in range(0,n):
	s=s+dummy[i]
for i in range(0,n):
	a[i]=dummy[i]/s


# initial resource distribution

dummy=[]
b=[]  # resource allocation
for i in range(0,n):
	dummy.append(random.random())
s=0
for i in range(0,n):
	s=s+dummy[i]
for i in range(0,n):
	b.append(dummy[i]/s)
for i in range(0,n):
	b[i]=b[i]*R

# resource allocation done




