import csv
from Graph import Graph
import Heap
from Movie import Movie


def main():
    # userSimilarMovie = input("Enter the movie you want to find something similar to ")
    userFavoriteActors = input("Enter the actor you want to watch today ")
    userFavoriteGenre = input("Enter your favorite genre ")
    userPreferredLength = input("Input whether you want a short movie (<90), medium movie (90-120), long (120+) ")
    howManySuggestions = int(input("Input how many suggestions you would like us to generate "))

    rows = []
    with open("moviedata/movies.csv", 'r') as file:
        reader = csv.reader(file)
        header = next(reader)
        try:
            for row in reader:
                rows.append(row)
        except UnicodeDecodeError:
            pass
    graph = populateGraph(rows)
    matchmaker(graph, userFavoriteGenre, userFavoriteActors, userPreferredLength, howManySuggestions)


def populateGraph(rows):
    graph = Graph()
    for i in range(len(rows)):  # for all rows of movies
        movie = Movie(rows[i][0], rows[i][2], rows[i][9], float(rows[i][14]), rows[i][5])
        graph.addVertex(movie)
    return graph


def matchmaker(graph, userFavoriteGenre, userFavoriteActors, userPreferredLength, howManySuggestions):
    idealMovie = Movie("", userFavoriteGenre, userFavoriteActors, userPreferredLength, 10)
    graph.addVertex(idealMovie)
    movies = graph.getEdges(idealMovie)
    movie_list = []
    while len(movie_list) < howManySuggestions:
        top = ""
        highestSim = 0
        for movie in movies:
            if movie.getSimilarity(idealMovie) > highestSim:
                if movie.movie not in movie_list and movie.movie != idealMovie.movie:
                    highestSim = movie.getSimilarity(idealMovie)
                    top = movie.movie
        movie_list.append(top)
    for movie in movie_list:
        print(movie)


if __name__ == '__main__':
    main()
