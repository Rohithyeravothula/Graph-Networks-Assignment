import Wattsstrogatz
import matplotlib.pyplot as plt
def get_clusteringcoeficient(adjacency_matrix,number_of_nodes,degree):  # adjacency matrix of given network node_number is number of nodes in network degree is list of degrees of each node
    d=[]
    for i in range(0,number_of_nodes):
        d.append(0)
    for i in range(0,number_of_nodes):
        c=0
        for j in range(0,number_of_nodes):
            for k in range(0,number_of_nodes):
                if i!=j and i!=k:
                    c=c+adjacency_matrix[i][j]*adjacency_matrix[i][k]*adjacency_matrix[k][j]
        c=c/2
        if degree[i]>1:
            coefficient=(2.0*c)/(degree[i]*(degree[i]-1))
        else:
            coefficient=0
        d[i]=coefficient
    return d
# clustering coefficient for nodes with degree <=1 is set to 0

def log_clustering_coefficient(list_avg_clusturing_coefficient):
    size=len(list_avg_clusturing_coefficient)
    s=""
    for i in range(0,size-1):
        s=s+str(list_avg_clusturing_coefficient[i])
        s=s+" "
    s=s+str(list_avg_clusturing_coefficient[size-1])+"\n"
    f=open("avg_clusturing_coefficient vs wiring_probability/Avg_clusturingcoefficient.txt",'w')
    f.write(s)
    f.close()
def plot_avg_cc(list_prob):  # list_prob is list of rewiring probability
    f=open("avg_clusturing_coefficient vs wiring_probability/Avg_clusturingcoefficient.txt",'r')
    s=f.read()
    avg_cc=map(float,s.split()) # avg_cc is the list of avg clustering coefficient
    plt.plot(list_prob,avg_cc,'ro')
    plt.xlabel("Re-wiring probability")
    plt.ylabel("Average clusturing coefficient")
    plt.title("average clusturing coefficient at various rewiring probabilities")
    plt.grid(True)
    plt.savefig("avg_clusturing_coefficient vs wiring_probability/plot_Log_avg_clusturingcoefficient")
    


lowerlimit_rewiring_probability=input("Enter the lower limit of rewiring probability (0.0 to 1.0): ")
change_rewiring_probability=input("Enter the differential value to change re wiring probability in each iteration (0.0 to 1.0) : ")
upperlimit_rewiring_probability=input("Enter the upper limit of rewiring probability (0.0 to 1.0): ")


graph=Wattsstrogatz.Graph()
rewiring_probabiliyt=upperlimit_rewiring_probability
count=1
list_cc=[]  # list of average clustering coefficients
list_prob=[]


while rewiring_probabiliyt>=lowerlimit_rewiring_probability:
    graph.generate_adj()
    graph.rewiring_probability=rewiring_probabiliyt
    list_prob.append(rewiring_probabiliyt)
    graph.watt_strogatz()
    degree=graph.get_degree()
    clusturing_coefficient=get_clusteringcoeficient(graph.adjacency_matrix, graph.number_of_nodes, degree)
    avg_clusturing_coefficient=sum(clusturing_coefficient)/len(clusturing_coefficient)
    list_cc.append(avg_clusturing_coefficient)
    count+=1
    rewiring_probabiliyt-=change_rewiring_probability

log_clustering_coefficient(list_cc)
plot_avg_cc(list_prob)
