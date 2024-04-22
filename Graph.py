import Movie
from collections import deque



class Graph:
    adj_list = {}

    def addVertex(self, key):
        self.adj_list[key] = []
        for vertex in self.adj_list:  # goes through each existing vertex in the graph
            for i in range(vertex.getSimilarity(key)):  # adds possibly multiple edges based on the similarity
                self.adj_list[key].append(vertex)
                self.adj_list[vertex].append(key)  # I think an undirected graph makes the most sense so add both ways?

    def addEdge(self, key, value):
        if key not in self.adj_list:
            self.adj_list[key] = []
        self.adj_list[key].append(value)

    def getEdges(self, key):
        edges = []
        for vertex in self.adj_list[key]:
            edges.append(vertex)
        return edges

    def bfs(self, source):
        visited = [False]  # * graph.size()
        visited[source] = True
        q = deque

        q.append(source)

        while q:
            current = q.popleft()
            for neighbor in self.adj_list:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    q.enqueue(neighbor)