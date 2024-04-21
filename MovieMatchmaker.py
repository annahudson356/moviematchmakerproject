import csv
from Graph import Graph
import Heap
from Movie import Movie


def main():
    userFavoriteActor = input("Enter the actor you want to watch today, if not type 0")
    userFavoriteGenre = input("Enter your favorite genre")
    userPreferredLength = float(input("Input whether you want a short movie (<90), medium movie (90-120), long (120+) "))
    howManySuggestions = input("Input how many suggestions you would like us to generate")

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
    matchmaker(graph, userFavoriteGenre, userFavoriteActor, userPreferredLength)

def populateGraph(rows):
    graph = Graph()
    for row in rows:
        movie = Movie(row[0], row[2], row[9], row[14],row[5]) # someone can double check i added the correct attributes according to dataset lol
        graph.addVertex(movie) # adds the movie AND adds edges to any similar existing movies (see graph class)
    return graph



def matchmaker(graph, userFavoriteGenre, userFavoriteActor, userPreferredLength):
    idealMovie = Movie("", userFavoriteGenre, userFavoriteActor, userPreferredLength, 10)
    graph.addVertex(idealMovie)
    movies = graph.getEdges(idealMovie)
    top = idealMovie
    highestSim = 0
    for movie, value in movies.items():
        if value > highestSim and movie.getMovie() != "":
            highestSim = value
            top = movie
    print(top.getMovie())




if __name__ == '__main__':
    main()

