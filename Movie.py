class Movie:
    def __init__(self, m, g, a, y, l, s):
        self.movie = m
        self.genre = g
        self.actors = a
        self.age = y
        self.length = l
        self.score = s
        if y == "old" or y == "new":
            self.age = y
        else:
            y = float(y)
        if isinstance(y, int):
            if 0 <= y < 2000:
                self.age = "old"
            elif 2000 <= y:
                self.age = "new"
            else:
                self.age = "unknown"
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

    def getMovie(self):
        return self.movie

    def getScore(self):
        return self.score

    def getSimilarity(self, movie2):
        # This could get ugly but we should have certain genres rank higher than others
        similarity = 0
        if movie2.genre == self.genre and movie2.genre != "" and self.genre != "":
            similarity += 4
        if movie2.length == self.length:
            similarity += 1
        if movie2.actors == self.actors and movie2.actors != "" and self.actors != "":
            similarity += 5
        if movie2.age == self.age:
            similarity += 3
        return similarity

