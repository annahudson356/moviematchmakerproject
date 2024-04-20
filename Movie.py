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

    def getSimilarity(self):
        pass