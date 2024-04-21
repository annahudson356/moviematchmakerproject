# import pandas
import Movie


class Graph:
    graph_pairs = [] # [(x,y),(i,j)]
    graph_al = {}  # empty dictionary, map isn't the same as in c++

    def insertEdge(self, movie_a, movie_b):
        if movie_a.genre == movie_b.genre:
            self.graph_pairs.append([movie_a, movie_b])
            self.graph_al = dict(self.graph_pairs)
        elif self.categorizeLength(movie_a) == self.categorizeLength(movie_b):  # don't really know if this is correct syntax at all
            self.graph_pairs.append([movie_a, movie_b])
            self.graph_al = dict(self.graph_pairs)
        else:
            for actor_a in movie_a.actors:
                for actor_b in movie_b.actors:
                    if actor_a == actor_b:
                        self.graph_pairs.append([movie_a, movie_b])
                        self.graph_al = dict(self.graph_pairs)  # transforms into a dict/map (adj list)

    def categorizeLength(self, movie):
        if 0 <= movie.length < 90:
            return "short"
        elif 90 <= movie.length < 120:
            return "medium"
        elif 120 <= movie.length:
            return "long"

    def bfs(self, source):
        pass
        # We could use this
