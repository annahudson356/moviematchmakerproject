class Movie:
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

    def getMovie(self):
        return self.movie

    def getScore(self):
        return self.score

    def compareActor(self, movie2):
        if self.actor == movie2.actor:
            return True
        return False

    def compareLength(self, movie2):
        if abs(float(self.length) - float(movie2.length)) < 30:
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
        if(movie2.length != "" and self.length != ""):
            if(abs(float(movie2.length) - float(self.length)) < 30):
                similarity += 1
        return similarity
