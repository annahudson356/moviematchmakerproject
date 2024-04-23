class Movie:
    def __init__(self, m, g, a, y, l, s):
        self.movie = m
        self.genre = g
        self.actors = a
        self.age = y
        self.length = l
        self.score = s

        if y.lower() == "old" or y.lower() == "new" or y.lower() == "":
            self.age = y
        else:
            y = float(y)
        if isinstance(y, float):
            if 0 <= y < 2000:
                self.age = "old"
            elif 2000 <= y:
                self.age = "new"
            else:
                self.age = "unknown"

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

    def getMovie(self):
        return self.movie

    def getScore(self):
        return self.score

    def getSimilarity(self, movie2):
        # This could get ugly but we should have certain genres rank higher than others
        similarity = 0
        if movie2.genre.lower() == self.genre.lower() and movie2.genre != "" and self.genre != "":
            similarity += 3
        else:
            # Determines the relevance of a genre compared to other genres
            if movie2.genre.lower() == "horror":
                if self.genre.lower() == "thriller":
                    similarity += 3
                if self.genre.lower() == "action":
                    similarity += 1
            elif movie2.genre.lower() == "drama":
                if self.genre.lower() == "romance":
                    similarity += 2
                if self.genre.lower() == "western":
                    similarity += 1
            elif movie2.genre.lower() == "adventure":
                if self.genre.lower() == "action":
                    similarity += 2
                if self.genre.lower() == "fantasy":
                    similarity += 1
            elif movie2.genre.lower() == "comedy":
                if self.genre.lower() == "adventure":
                    similarity += 1
            elif movie2.genre.lower() == "action":
                if self.genre.lower() == "adventure":
                    similarity += 2
                if self.genre.lower() == "fantasy":
                    similarity += 1
            elif movie2.genre.lower() == "biography":
                if self.genre.lower() == "crime":
                    similarity += 1
            elif movie2.genre.lower() == "crime":
                if self.genre.lower() == "thriller":
                    similarity += 2
                if self.genre.lower() == "biography":
                    similarity += 1
            elif movie2.genre.lower() == "fantasy":
                if self.genre.lower() == "adventure":
                    similarity += 2
                if self.genre.lower() == "action":
                    similarity += 1
            elif movie2.genre.lower() == "family":
                if self.genre.lower() == "comedy":
                    similarity += 2
                if self.genre.lower() == "adventure":
                    similarity += 1
            elif movie2.genre.lower() == "sci-fi":
                if self.genre.lower() == "thriller":
                    similarity += 2
                if self.genre.lower() == "action":
                    similarity += 1
            elif movie2.genre.lower() == "animation":
                if self.genre.lower() == "family":
                    similarity += 2
            elif movie2.genre.lower() == "thriller":
                if self.genre.lower() == "horror":
                    similarity += 3
                if self.genre.lower() == "sci-fi":
                    similarity += 2
                if self.genre.lower() == "western":
                    similarity += 1
            elif movie2.genre.lower() == "western":
                if self.genre.lower() == "romance":
                    similarity += 2
                if self.genre.lower() == "biography":
                    similarity += 1
            elif movie2.genre.lower() == "romance":
                if self.genre.lower() == "drama":
                    similarity += 2
                if self.genre.lower() == "comedy":
                    similarity += 1

        if movie2.length.lower() == self.length.lower():
            similarity += 1
        if movie2.actors.lower() == self.actors.lower() and movie2.actors != "" and self.actors != "":
            similarity += 4
        if movie2.age.lower() == self.age.lower():
            similarity += 2

        return similarity

