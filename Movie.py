class Movie:
    def __init__(self, m, g, a, y, l, s): # constructor to initialize each variable of the movie
        self.movie = m
        self.genre = g
        self.actors = a
        self.age = y
        self.length = l
        self.score = s

        if y.lower() == "old" or y.lower() == "new" or y.lower() == "": # to initialize the age from user input
            self.age = y
        else:
            y = float(y)
        if isinstance(y, float): # to initialize the number year from the dataset into an age string
            if 0 <= y < 2000:
                self.age = "old"
            elif 2000 <= y:
                self.age = "new"
            else:
                self.age = "unknown"

        if l.lower() == "short" or l.lower() == "medium" or l.lower() == "long" or l == "": # to initialize the length from user input
            self.length = l
        else:
            l = float(l)
        if isinstance(l, float): # to initialize the number length from the dataset into an length string
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

    def getSimilarity(self, movie2): # adds points to the similarity between 2 movies based on which traits are equal
        similarity = 0
        if movie2.genre.lower() == self.genre.lower() and movie2.genre != "" and self.genre != "":
            similarity += 3
        if movie2.length.lower() == self.length.lower() and movie2.length != "unknown" and self.length != "unknown":
            similarity += 1
        if movie2.actors.lower() == self.actors.lower() and movie2.actors != "" and self.actors != "":
            similarity += 4
        if movie2.age.lower() == self.age.lower() and movie2.age != "unknown" and self.age != "unknown":
            similarity += 2
        return similarity

