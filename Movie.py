class Movie:
    movie = ""
    genre = ""
    actor = "" # the dataset only gives the star actor, not multiple, so i changed from array to string
    length = 0
    score = 0 # added score b/c we should recommend similar movies with the highest scores

    def __init__(self, m, g, a, l, s):
        self.movie = m
        self.genre = g
        self.actors = a
        self.length = l
        self.score = s

    def compareGenre(self, movie2):
        if self.genre == movie2.genre:
            return True
        return False

    def compareActor(self, movie2):
        if self.actor == movie2.actor:
            return True
        return False

    def compareLength(self, movie2):
        if abs(self.length - movie2.length) < 30:
            return True
        return False


    def getSimilarity(self, movie2): # just a rough idea
        similarity = 0
       # if(movie2.movie==self.movie): # i dont think having this makes sense actually cause they dont want the same movie name lol
          #  similarity += 1
        if(movie2.genre==self.genre):
            similarity += 1
        if(movie2.actors==self.actors):
            similarity += 1
        if(movie2.length==self.length):
            similarity += 1
        return similarity
