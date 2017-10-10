import matplotlib.pyplot as plt
number=11
for i in range(0,number):
	f=open("data"+str(i)+".txt")
	s=f.read()
	x=map(float,s.split("\n"))
	y=[]
	l=len(x)
	f.close()
	f=open("degree.txt",'r')
	s=f.read()
	y=map(int,s.split("\n")
	plt.plot(y,x)
	plt.show()