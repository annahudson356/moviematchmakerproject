import csv
from datetime import datetime
from Graph import Graph
from Heap import Heap
from Movie import Movie



def main():
    graphRunningSum = 0
    heapRunningSum = 0
    print("Welcome to Movie Matchmaker! Please follow the prompts below to be matched to your ideal movie! Please make "
          "sure to watch capitalization!\n\n NOTE: We use the data to enter to find the most similar movie across all aspects"
          ", not necessarily the movie that matches everything exactly!")
    while True:
        toExit = input("Press ENTER to continue, any other key to exit: ")
        if toExit != "":
            print("\n\n\nThanks for using Movie MatchMaker!")
            print("--------------------\nCredits: \n")
            print("Chloe Bai\nNora Choukri\nAnna Hudson")
            break

        # userSimilarMovie = input("Enter the movie you want to find something similar to ")
        userFavoriteActors = input("Enter one actor you want to watch today ")
        userFavoriteGenre = input("Enter your favorite genre: ")
        userPreferredLength = input("Input whether you want a short movie (<90), medium movie (90-120), long (120+): ")
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

            # Times the Graph Creation
            a = datetime.now()
            graph = populateGraph(rows)
            b = datetime.now()
            time = b - a
            graphRunningSum += time.total_seconds()


            # Times the Heap Creation
            a = datetime.now()
            movieHeap = populateHeap(rows)
            b = datetime.now()
            time = b - a
            heapRunningSum += time.total_seconds()


            # Does the Matchmaking process

            # Times the graph matchmaking process
            print("Matchmaking using a graph: \n")
            a = datetime.now()
            matchGraph(graph, userFavoriteGenre, userFavoriteActors, userPreferredLength, howManySuggestions)
            b = datetime.now()
            time = b - a
            graphRunningSum += time.total_seconds()


            # Times the heap matchmaking process
            print("Matchmaking using a heap: \n")
            a = datetime.now()
            matchHeap(movieHeap, userFavoriteGenre, userFavoriteActors, userPreferredLength, howManySuggestions)
            b = datetime.now()
            time = b - a
            heapRunningSum += time.total_seconds()


            print("Graph Total Time: " + str(graphRunningSum))
            print("Heap Total Time: " + str(heapRunningSum))
            print("Which was faster? " + "Heap" if heapRunningSum < graphRunningSum else "Graph")
        except ValueError:
            print("Invalid Input! Please Try Again!\n\n\n")
            continue


def populateGraph(rows):
    graph = Graph()
    for i in range(len(rows)):  # for all rows of movies
        movie = Movie(rows[i][0], rows[i][2], rows[i][9], float(rows[i][14]), rows[i][5])
        graph.addVertex(movie)
    return graph




def populateHeap(rows):
    heap = Heap()
    for i in range(len(rows)):
        if rows[i][14] == "":
            movie = Movie(rows[i][0], rows[i][2], rows[i][9], -1, rows[i][5])
        else:
            movie = Movie(rows[i][0], rows[i][2], rows[i][9], float(rows[i][14]), rows[i][5])
        heap.getArr().append(movie)

    heap.heapifyDown(0)
    return heap


def matchGraph(graph, userFavoriteGenre, userFavoriteActors, userPreferredLength, howManySuggestions):
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


def matchHeap(heap, userFavoriteGenre, userFavoriteActors, userPreferredLength, howManySuggestions):
    idealMovie = Movie("", userFavoriteGenre, userFavoriteActors, userPreferredLength, 1000)
    tempMovie = Movie("", userFavoriteGenre, userFavoriteActors, userPreferredLength, 0)
    highestSim = idealMovie
    heap.getArr().append(idealMovie)
    for movie in heap.getArr():
        if movie.getSimilarity(idealMovie) > highestSim.getSimilarity(idealMovie):
            if movie.movie not in heap.getArr() and movie.getMovie() != idealMovie.movie:
                highestSim = movie.movie

    heap.heapifyDown(heap.getArr().index(highestSim))
    for i in range(0, int(howManySuggestions)):
        print(heap.extractMax())


if __name__ == '__main__':
    main()
