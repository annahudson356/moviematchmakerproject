class Movie:
    def __init__(self, m, g, a, l, s):
        self.movie = m
        self.genre = g
        self.actors = a
        if l.lower() == "short" or l.lower() == "medium" or l.lower() == "long" or l == "":
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
        if movie2.genre.lower() == self.genre.lower() and movie2.genre != "" and self.genre != "":
            similarity += 2
        if movie2.length.lower() == self.length.lower():
            similarity += 1
        if movie2.actors.lower() == self.actors.lower() and movie2.actors != "" and self.actors != "":
            similarity += 5
        return similarity

