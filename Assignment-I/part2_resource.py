# import start 

import random
import math 

# import end

# definition start

n=1000  # number of individuals
t=10# number of time stamps
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


# initia resource allocation 
b=avg_dist(R)
#b=random_dist(R)


def snapshot(b,snapshot_count):
	z="part2_2/data"+str(snapshot_count)+".txt"
	f=open(z,'w')
	for i in range(0,n-1):
		f.write(str(b[i])+"\n")
	f.write(str(b[n-1]))
	f.close()


def gen_depend_graph(n,e):  # n is # nodes e is # edges graph is directedg graph
	graph=[]
	for i in range(0,n):
		dummy=[]
		for j in range(0,n):
			dummy.append(0)
		graph.append(dummy)
	count=0
	while True:
		u=int(random.random()*n)
		v=int(random.random()*n)
		if u!=v and graph[u][v]!=1:
			graph[u][v]=1
			count=count+1
		if count==e:
			break
	return graph


def exp_growth(b,const,power_a,power_b,power_c):
	for i in range(0,n):
		z=1
		for j in range(0,n):
			if graph[i][j]==1:
				z=z*math.pow(b[j],power_c)
		b[i]=b[i]+const*math.pow(a[i],power_a)*math.pow(b[i],power_b)*z
		

graph=gen_depend_graph(n,n+(n/2))
#print graph

# put degree to file
degree=[]
for i in range(0,n):
	degree.append(sum(graph[i]))
f=open("part2_2/degree.txt",'w')
for i in range(0,n-1):
	f.write(str(degree[i])+"\n")
f.write(str(degree[n-1]))
f.close()

#



time=0
snapshot_count=0
while True:
	#print b
	if time==t:
		break
	if time%snap==0:
		snapshot(b,snapshot_count)
		snapshot_count=snapshot_count+1
	time=time+1
	exp_growth(b,2,1,1.1,0.5)


print "The End"





