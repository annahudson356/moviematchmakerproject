class Movie:
    movie = ""
    genre = ""
    actor = "" # the dataset only gives the star actor, not multiple, so i changed from array to string
    length = 0
    score = 0 # addes score b/c we should recommend similar movies with the highest scores

    def __init__(self, m, g, a, l, s):
        self.movie = m
        self.genre = g
        self.actors = a
        self.length = l
        self.score = s

    def getSimilarity(self, movie2): # just a rough idea
        similarity = 0
        if(movie2.movie==self.movie):
            similarity += 1
        if(movie2.genre==self.genre):
            similarity += 1
        if(movie2.actors==self.actors):
            similarity += 1
        if(movie2.length==self.length):
            similarity += 1
        return similarity
