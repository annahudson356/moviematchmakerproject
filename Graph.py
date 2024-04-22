import Movie
from collections import deque



class Graph:
    adj_list = {}

    def addVertex(self, key):
        self.adj_list[key] = []
        for vertex in self.adj_list:  # goes through each existing vertex in the graph
            for i in range(vertex.getSimilarity(key)):  # adds possibly multiple edges based on the similarity
                self.adj_list[key].append(vertex)
                self.adj_list[vertex].append(key)  # undirected graph so add both ways

    def getEdges(self, key): # returns all the edges of the vertex
        edges = []
        for vertex in self.adj_list[key]:
            edges.append(vertex)
        return edges

