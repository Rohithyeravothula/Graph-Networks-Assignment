import math
import random
import networkx as nx
import matplotlib.pyplot as plt


class Graph:
    def __init__(self):
        self.number_of_nodes=input("Enter the number of nodes in graph for simulation")
        self.degree_of_nodes=input("Enter the regularity of graph")
    def getrewiringprobability(self):  # take rewiring probability from stdin
        self.rewiring_probability=input("Rewiring probability")
    def generate_adj(self):  # generate adjacency matrix for given number f nodes and degree from stdin
        self.adjacency_matrix=[[0 for x in range(self.number_of_nodes)] for y in range(self.number_of_nodes)]
        for i in range(0,self.number_of_nodes):
            for j in range(1,1+self.degree_of_nodes-(self.degree_of_nodes/2)):
                self.adjacency_matrix[i][(i+j)%self.number_of_nodes]=1
                self.adjacency_matrix[(i+j)%self.number_of_nodes][i]=1
        
    def count_degree(self):  # count total degree count in the network
        c=0
        for i in range(0,self.number_of_nodes):
            for j in range(0,self.number_of_nodes):
                if self.adjacency_matrix[i][j]==1:
                    c+=1
        return c
    def draw_graph(self):  # a is adjacency matrix of network and n is size of network
        G=nx.Graph()
        for i in range(0,self.number_of_nodes):
            G.add_node(i)
        for i in range(0,self.number_of_nodes):
            for j in range(0,i):
                if self.adjacency_matrix[i][j]==1:
                    G.add_edge(i,j)
        pos = nx.shell_layout(G)
        nx.draw(G, pos)
        plt.show()

    def print2(self):  # function to print 2d arraylist in table format
        for i in range(0,self.number_of_nodes):
            print a[i]

    def get_degree(self): # returns list of degree of each node
        d=[]
        for i in range(0,self.number_of_nodes):
            d.append(0)
        for i in range(0,self.number_of_nodes):
            d[i]=sum(self.adjacency_matrix[i])
        return d
                
    
    def watt_strogatz(self): # a is network adjacency matrix n is size of network B is rewiring probability
        for j in range(1,1+self.degree_of_nodes-(self.degree_of_nodes/2)):
            for i in range(0,self.number_of_nodes):
                rand1=random.random()
                if rand1<self.rewiring_probability:
                    self.adjacency_matrix[i][(i+j)%self.number_of_nodes]=0
                    self.adjacency_matrix[(i+j)%self.number_of_nodes][i]=0
                    while True:    # need to check if graph is not completely connected
                        rand_node=int(random.random()*self.number_of_nodes)
                        if i!=rand_node and self.adjacency_matrix[i][rand_node]!=1:
                            self.adjacency_matrix[i][rand_node]=1
                            self.adjacency_matrix[rand_node][i]=1
                            break
                #print "removed at "+str(i)+" "+str((i+j)%n)+" added at "+str(i)+" "+str(rand_node)
    
                
# if rewiring_probability ==0 the network stays unchanged if ==1 network turns out to be random network



def main():
    graph=Graph()
    graph.generate_adj()
    graph.draw_graph()
    graph.getrewiringprobability()
    graph.watt_strogatz()
    graph.draw_graph()
    
if __name__=="__main__":
    main()