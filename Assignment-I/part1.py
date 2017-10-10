# import start 

import random
import math 

# import end

# definition start

n=1000  # number of individuals
t=1000 # number of time stamps
R=10000 # resources
snap=t/10
# definition end

# abilities 

a=[] #ability
for i in range(0,n):
	a.append(random.random())


# function definitions

def avg_dist(R):
	b=[]
	for i in range(0,n):
		b.append((R*1.0)/n)
	return b
def random_dist(R):
	dummy=[]
	b=[]  # resource allocation
	for i in range(0,n):
		dummy.append(random.random())
	s=sum(dummy)
	for i in range(0,n):
		b.append(dummy[i]/s)
	for i in range(0,n):
		b[i]=b[i]*R
	return b

def snapshot(b,snapshot_count):
	z="part1/data"+str(snapshot_count)+".txt"
	f=open(z,'w')
	for i in range(0,n-1):
		f.write(str(b[i])+"\n")
	f.write(str(b[n-1]))
	f.close()

def exp_growth(b,const,power_a,power_b):  # power_a ability power  power_b is resource power
	l=len(b)
	for i in range(0,l):
		b[i]=b[i]+const*math.pow(a[i],power_a)*math.pow(b[i],power_b)   
def logfile(b):
	f=open("part1/logfile.txt",'a')
	s=""
	for i in range(0,n-1):
		s=s+str(b[i])+" "
	s=s+str(b[n-1])+"\n"
	f.write(s)
	f.close()

# resource allocation 
b=avg_dist(R)
#b=random_dist(R)


snapshot_count=0
time=0
while True:
	if time%snap==0:
		snapshot(b,snapshot_count)
		snapshot_count=snapshot_count+1
	if time==t:
		break
	exp_growth(b,2,7,0.8)  # fun(resource, const, powerof ability, power of resource)
	time=time+1
	logfile(b)

print "The End"




