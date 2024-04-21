import csv
from datetime import datetime
from Graph import Graph
from Heap import Heap
from Movie import Movie


def main():
    print("Welcome to Movie Matchmaker! Please follow the prompts below to be matched to your ideal movie!\n\n")
    while True:
        toExit = input("Press ENTER to continue, any other key to exit: ")
        if toExit != "":
            print("\n\n\nThanks for using Movie MatchMaker!")
            print("--------------------\nCredits: \n")
            print("Chloe Bai\nNora Choukri\nAnna Hudson")
            break

        # userSimilarMovie = input("Enter the movie you want to find something similar to ")
        userFavoriteActors = input("Enter one actor you want to watch today ")
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

        try:
            # Creates the graph and the heap data structure
            graph = populateGraph(rows)
            movieHeap = populateHeap(rows)

            # Does the Matchmaking process
            matchGraph(graph, userFavoriteGenre, userFavoriteActors, userPreferredLength, howManySuggestions)
            matchHeap(movieHeap, userFavoriteGenre, userFavoriteActors, userPreferredLength, howManySuggestions)

            print("Data Collection: Was the Heap faster than the Graph?")
            print(matchGraph(graph, userFavoriteGenre, userFavoriteActors, userPreferredLength,
                             howManySuggestions) >
                  matchHeap(movieHeap, userFavoriteGenre, userFavoriteActors, userPreferredLength))
        except ValueError:
            print("Invalid Input! Please Try Again!\n\n\n")
            continue


def populateGraph(rows):
    time_a = datetime.now()
    graph = Graph()
    for i in range(len(rows)):  # for all rows of movies
        movie = Movie(rows[i][0], rows[i][2], rows[i][9], float(rows[i][14]), rows[i][5])
        graph.addVertex(movie)
    time_b = datetime.now()
    print("Time taken to build the graph: " + str(time_b - time_a))
    return graph


def populateHeap(rows):
    time_a = datetime.now()
    heap = Heap()
    for i in range(len(rows)):
        if rows[i][14] == "":
            movie = Movie(rows[i][0], rows[i][2], rows[i][9], -1, rows[i][5])
        else:
            movie = Movie(rows[i][0], rows[i][2], rows[i][9], float(rows[i][14]), rows[i][5])
        heap.getArr().append(movie)
    heap.heapifyDown(0)
    time_b = datetime.now()
    print("Time taken to build the heap: " + str(time_b - time_a))
    return heap


def matchGraph(graph, userFavoriteGenre, userFavoriteActors, userPreferredLength, howManySuggestions):
    time_a = datetime.now()
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
    time_b = datetime.now()
    print("Time taken to find your ideal movie using the graph: " + str(time_b - time_a))
    return time_b - time_a


def matchHeap(heap, userFavoriteGenre, userFavoriteActors, userPreferredLength, howManySuggestions):
    time_a = datetime.now()
    heap.kthLargestElements(howManySuggestions)
    time_b = datetime.now()
    print("Time taken to find your ideal movie using the heap: " + str(time_b - time_a))
    return time_b - time_a


if __name__ == '__main__':
    main()
