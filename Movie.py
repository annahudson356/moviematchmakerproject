class Movie:
    def __init__(self, m, g, a, l, s):
        self.movie = m
        self.genre = g
        self.actors = a
        if l == "short" or l == "medium" or l == "long" or l == "":
            self.length = l
        else:
            l = float(l)
        if isinstance(l, float):
            if 0 <= l < 90:
                self.length = "short"
            elif 90 <= l < 120:
                self.length = "medium"
            elif 120 <= l:
                self.length = "long"
            else:
                self.length = "unknown"
        self.score = s

    def getMovie(self):
        return self.movie

    def getScore(self):
        return self.score

    def getSimilarity(self, movie2):
        # This could get ugly but we should have certain genres rank higher than others
        similarity = 0
        if movie2.genre == self.genre:
            similarity += 20
        if movie2.length == self.length:
            similarity += 10
        if movie2.actors == self.actors:
            similarity += 50
        return similarity
