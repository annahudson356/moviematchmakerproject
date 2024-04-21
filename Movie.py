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
        if l == "short" or l == "medium" or l == "long":
            self.length = l
        elif 0 <= l < 90:
            self.length = "short"
        elif 90 <= l < 120:
            self.length = "medium"
        elif 120 <= l:
            self.length = "long"
        self.score = s

    def getSimilarity(self, movie2):
        similarity = 0
        if movie2.genre == self.genre:
            similarity += 1
        if movie2.length == self.length:
            similarity += 1
        for actor in self.actors:
            for actor2 in movie2.actors:
                if actor == actor2:
                    similarity += 1
        return similarity
