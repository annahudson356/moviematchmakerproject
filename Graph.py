# import pandas
class Graph:
    class Vertex:
        similarity = 0
        class Movie:
            movie = ""
            genre = ""
            actors = []
            length = 0

            def __init__(self, m, g, a, l):
                self.movie = m
                self.genre = g
                self.actors = a
                self.length = l

    genre_pairs = []
    actor_pairs = []
    length_pairs = [] # [(x,y),(i,j)]
    genre_al = {}  # empty dictionary, map isn't the same as in c++
    actor_al = {}
    length_al = {}

    def insertGenreEdge(self, movie_a, movie_b):  # movie_a + movie_b are "match" movies
        self.genre_pairs.append([movie_a, movie_b])
        self.genre_al = dict(self.genre_pairs)  # transforms into a dict/map (adj list)
        # three separate graphs for each attribute comparing "match worthiness"
        pass

    def insertActorEdge(self, movie_a, movie_b):
        self.actor_pairs.append([movie_a, movie_b])
        self.actor_al = dict(self.actor_pairs)
        pass

    def insertLengthEdge(self, movie_a, movie_b):
        self.length_pairs.append([movie_a, movie_b])
        self.length_al = dict(self.length_pairs)
        pass

    def make
    def bfs(self, source):
        pass
        # We could use this

