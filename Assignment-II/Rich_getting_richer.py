import Wattsstrogatz
import matplotlib.pyplot as plt
import random
import networkx as nx
import math


def draw_graph(adjacency_matrix):  # a is adjacency matrix of network and n is size of network
    G=nx.Graph()
    number_of_nodes=len(adjacency_matrix)
    for i in range(0,number_of_nodes):
        G.add_node(i)
    for i in range(0,number_of_nodes):
        for j in range(0,i):
            if adjacency_matrix[i][j]==1:
                G.add_edge(i,j)
    pos = nx.shell_layout(G)
    nx.draw(G, pos)
    plt.show()
def append_new_node(adjacency_matrix):
    lenght=len(adjacency_matrix)
    for i in range(0,lenght):
        adjacency_matrix[i].append(0)
    dummy=[0 for i in range(lenght+1)]
    adjacency_matrix.append(dummy)
    return adjacency_matrix
def rich_getting_richer():
    graph=Wattsstrogatz.Graph()
    graph.getrewiringprobability()
    graph.generate_adj()
    graph.watt_strogatz()
    degree=graph.get_degree()  # contains the list of degree
    for i in range(0,graph.number_of_nodes):
        normalized_degree=[]
        sum_degree=sum(degree)
        size=len(degree)
        for j in range(0,size):
            normalized_degree.append((1.0*degree[j])/sum_degree)
        graph.adjacency_matrix=append_new_node(graph.adjacency_matrix)
        degree.append(0)
        while  degree[graph.number_of_nodes+i]<1:
            #draw_graph(graph.adjacency_matrix)
            #print normalized_degree
            rand=math.sqrt(random.random())   # random probability generated to make rewiring and new connections
            #print rand
            for j in range(0,size):
                if rand<=normalized_degree[j] and i!=j:
                    degree[j]+=1 # increase the degree of i th node by 1
                    degree[graph.number_of_nodes+i]+=1
                    graph.adjacency_matrix[j][graph.number_of_nodes+i]=1
                    graph.adjacency_matrix[graph.number_of_nodes+i][j]=1
    
    return [graph.adjacency_matrix,degree]

def plot_degree_distribution(degree):
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
    for i in range(0,l):
        degree_abs[i]=math.log(degree_abs[i],2)
        degree_freq[i]=math.log(degree_freq[i],2)
    plt.plot(degree_abs,degree_freq,'ro')
    plt.show()

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

def log_clustering_coefficient(list_avg_clusturing_coefficient):
    size=len(list_avg_clusturing_coefficient)
    s=""
    for i in range(0,size-1):
        s=s+str(list_avg_clusturing_coefficient[i])
        s=s+" "
    s=s+str(list_avg_clusturing_coefficient[size-1])+"\n"
    f=open("Rich getting richer/Avg_clusturingcoefficient.txt",'w')
    f.write(s)
    f.close()
def plot_avg_cc(list_prob):  # list_prob is list of rewiring probability
    f=open("Rich getting richer/Avg_clusturingcoefficient.txt",'r')
    s=f.read()
    avg_cc=map(float,s.split()) # avg_cc is the list of avg clustering coefficient
    plt.plot(list_prob,avg_cc,'ro')
    plt.xlabel("Re-wiring probability")
    plt.ylabel("Average clusturing coefficient")
    plt.title("average clusturing coefficient at various rewiring probabilities")
    plt.grid(True)
    plt.savefig("Rich getting richer/plot_Log_avg_clusturingcoefficient")
    
def clusturing_coeff():
    count=0
    while count<10:
        count+=1
        rich_getting_richer()
        clusturing_coefficient=get_clusteringcoeficient(adjacency_matrix,len(adjacency_matrix), degree)
        list_avg_clusturing_coefficient=sum(clusturing_coefficient)/len(clusturing_coefficient)         
        log_clustering_coefficient(list_avg_clusturing_coefficient)
        plot_avg_cc()

output=rich_getting_richer()
adjacency_matrix=output[0]
degree=output[1]
plot_degree_distribution(degree)

