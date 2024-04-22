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
            similarity += 5
        else:
            # Determines the relevance of a genre compared to other genres
            if movie2.genre.lower() == "Horror":
                if self.movie.genre == "Thriller":
                    similarity += 3
                if self.movie.genre == "Action":
                    similarity += 2
            elif movie2.genre.lower() == "Drama":
                if self.movie.genre == "Romance":
                    similarity += 3
                if self.movie.genre == "Western":
                    similarity += 2
            elif movie2.genre.lower() == "Adventure":
                if self.movie.genre == "Action":
                    similarity += 3
                if self.movie.genre == "Fantasy":
                    similarity += 2
            elif movie2.genre.lower() == "Comedy":
                if self.movie.genre == "Family":
                    similarity += 3
                if self.movie.genre == "Adventure":
                    similarity += 2
            elif movie2.genre.lower() == "Action":
                if self.movie.genre == "Adventure":
                    similarity += 3
                if self.movie.genre == "Fantasy":
                    similarity += 2
            elif movie2.genre.lower() == "Biography":
                if self.movie.genre == "Crime":
                    similarity += 3
            elif movie2.genre.lower() == "Crime":
                if self.movie.genre == "Thriller":
                    similarity += 3
                if self.movie.genre == "Biography":
                    similarity += 2
            elif movie2.genre.lower() == "Fantasy":
                if self.movie.genre == "Adventure":
                    similarity += 3
                if self.movie.genre == "Action":
                    similarity += 2
            elif movie2.genre.lower() == "Family":
                if self.movie.genre == "Comedy":
                    similarity += 3
                if self.movie.genre == "Adventure":
                    similarity += 2
            elif movie2.genre.lower() == "Sci-Fi":
                if self.movie.genre == "Thriller":
                    similarity += 3
                if self.movie.genre == "Action":
                    similarity += 2
            elif movie2.genre.lower() == "Animation":
                if self.movie.genre == "Family":
                    similarity += 3
            elif movie2.genre.lower() == "Thriller":
                if self.movie.genre == "Sci-Fi":
                    similarity += 3
                if self.movie.genre == "Western":
                    similarity += 2
            elif movie2.genre.lower() == "Western":
                if self.movie.genre == "Romance":
                    similarity += 3
                if self.movie.genre == "Biography":
                    similarity += 2
            elif movie2.genre.lower() == "Romance":
                if self.movie.genre == "Drama":
                    similarity += 3
                if self.movie.genre == "Fantasy":
                    similarity += 2

        if movie2.length.lower() == self.length.lower():
            similarity += 2
        if movie2.actors.lower() == self.actors.lower() and movie2.actors != "" and self.actors != "":
            similarity += 6
        if movie2.age.lower() == self.age.lower():
            similarity += 4
        if float(self.score) > 7.0:
            similarity += 3

        return similarity

