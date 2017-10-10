import Wattsstrogatz
import matplotlib.pyplot as plt

def logdegree(degree,n,count):
    s=""
    for i in range(0,n-1):
        s=s+str(degree[i])
        s=s+" "
    s=s+str(degree[n-1])+"\n"
    f=open("Degree distribution vs wiring probability/Degree"+str(count)+".txt",'w')
    f.write(s)
    f.close()

def plotdegree_vs_rewiringprobability(file_count,prob_list):
    count=1  # corresponding to number of files to be read
    index=0  # corresponding to rewiring probability
    while count<file_count:
        f=open("Degree distribution vs wiring probability/Degree"+str(count)+".txt","r")
        x=f.read()
        degree=[]
        degree=map(int,x.split())
        degree_map={}
        degree_abs=[]
        l=len(degree)
        for i in range(0,l):
            try:
                if degree_map[degree[i]]>0:
                    degree_map[degree[i]]+=1
            except:
                degree_abs.append(degree[i])
                degree_map[degree[i]]=1
        degree_freq=[]
        l=len(degree_abs)
        for i in range(0,l):
            degree_freq.append(degree_map[degree_abs[i]])
        xmin=min(degree_abs)-10
        xmax=max(degree_abs)+10
        ymin=min(degree_freq)-10
        ymax=max(degree_freq)+10
        plt.axis([xmin,xmax,ymin,ymax]) # sets the min max points of the plot on x_axis and y_axis
        plt.plot(degree_abs,degree_freq,'ro')
        plt.xlabel("Degree (K)")
        plt.ylabel("# of nodes with degree k")
        plt.title("Degree distribution at wiring probability "+str(prob_list[index]))
        plt.savefig("Degree distribution vs wiring probability/plot_degree"+str(count))
        count+=1
        index+=1
        

    
lowerlimit_rewiring_probability=input("Enter the lower limit of rewiring probability (0.0 to 1.0): ")
change_rewiring_probability=input("Enter the differential value to change re wiring probability in each iteration (0.0 to 1.0) : ")
upperlimit_rewiring_probability=input("Enter the upper limit of rewiring probability (0.0 to 1.0): ")


graph=Wattsstrogatz.Graph()
rewiring_probability=upperlimit_rewiring_probability
prob_list = []  # contains rewiring probabilities
count=1
while rewiring_probability>=lowerlimit_rewiring_probability:
    graph.generate_adj()
    graph.rewiring_probability=rewiring_probability
    graph.watt_strogatz()
    prob_list.append(rewiring_probability)
    rewiring_probability-=change_rewiring_probability
    degree=graph.get_degree()
    logdegree(degree,graph.number_of_nodes,count)
    count+=1
plotdegree_vs_rewiringprobability(count,prob_list)