import matplotlib.pyplot as plt
number=10
for i in range(0,number):
	f=open("data"+str(i)+".txt")
	s=f.read()
	x=map(float,s.split("\n"))
	y=[]
	l=len(x)
	for j in range(0,l):
		y.append(j)
	plt.plot(y,x)
	plt.show()
