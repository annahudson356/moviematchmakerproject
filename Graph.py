# import pandas
import Movie
from collections import deque


class Graph:

    def __init__(self):
        self.adj_list = {}

    def addVertex(self, key):
        self.adj_list[key] = []
        for vertex in self.adj_list: # goes thru each existing vertex in the graph
            for i in range(vertex.getSimilarity(key)): # adds possibly multiple edges based on the similarity (see movie class)
                self.adj_list[key].append(vertex)
                self.adj_list[vertex].append(key) # I think an undirected graph makes the most sense so add both ways?


    def addEdge(self, key, value):
        if key not in self.adj_list:
            self.adj_list[key] = []
        self.adj_list[key].append(value)

    def getEdges(self, key):
        edges = {}
        for vertex in self.adj_list[key]:
            if vertex not in edges:
                edges[vertex] = 0
            edges[vertex] += 1
        return edges

    def bfs(self, source):
        visited = [False]  # * graph.size()
        visited[source] = True
        q = deque

        q.append(source)

        while q:
            current = q.popleft()
        '''    # action with current node
            for neighbor in  # something? not really sure I understand the graph implementation:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    q.append(neighbor) '''


