import networkx as nx
import matplotlib.pyplot as plt
import Wattsstrogatz

def get_char_pathlenght(adjacency_matrix,number_of_nodes):
    G=nx.Graph()
    for i in range(0,number_of_nodes):
        G.add_node(i)
    for i in range(0,number_of_nodes):
        for j in range(0,number_of_nodes):
            if adjacency_matrix[i][j]==1:
                G.add_edge(i, j)
    return nx.average_shortest_path_length(G)
    

def log_pathlenght(path_lenghtlist):
    size=len(path_lenghtlist)
    s=""
    for i in range(0,size-1):
        s=s+str(path_lenghtlist[i])+" "
    s=s+str(path_lenghtlist[size-1])+"\n"
    f=open("characteristic  pathlenght/Avg_pathlenght.txt",'w')
    f.write(s)
def plot_pathlenght_vs_rewiring_probability(prob_list):
    f=open("characteristic  pathlenght/Avg_pathlenght.txt",'r')
    x=f.read()
    avg_pathlist=map(float,x.split())
    #x_min=int(min(prob_list))-2
    #x_max=int(max(prob_list))+2
    #y_min=int(min(avg_pathlist))-2
    #y_max=int(max(avg_pathlist))+2
    plt.plot(prob_list,avg_pathlist,'ro')
    #plt.axis([x_min,x_max,y_min,y_max])
    plt.xlabel("Re-wiring Probability")
    plt.ylabel("Chareterstic Path lenght")
    plt.savefig("characteristic  pathlenght/plot_Avg_pathlenght")
    


lowerlimit_rewiring_probability=input("Enter the lower limit of rewiring probability (0.0 to 1.0): ")
change_rewiring_probability=input("Enter the differential value to change re wiring probability in each iteration (0.0 to 1.0) : ")
upperlimit_rewiring_probability=input("Enter the upper limit of rewiring probability (0.0 to 1.0): ")


graph=Wattsstrogatz.Graph()
rewiring_probability=upperlimit_rewiring_probability
path_lenghtlist=[]  # contains path lengths
prob_list=[] 
while rewiring_probability>=lowerlimit_rewiring_probability:
    graph.generate_adj()
    graph.rewiring_probability=rewiring_probability
    graph.watt_strogatz()
    avg_path_lenght=get_char_pathlenght(graph.adjacency_matrix, graph.number_of_nodes)
    prob_list.append(rewiring_probability)
    path_lenghtlist.append(avg_path_lenght)
    rewiring_probability-=change_rewiring_probability
log_pathlenght(path_lenghtlist)
plot_pathlenght_vs_rewiring_probability(prob_list)