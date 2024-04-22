import csv
from datetime import datetime
from Graph import Graph
from Heap import Heap
from Movie import Movie



def main():
    graphRunningSum = 0
    heapRunningSum = 0
    print("Welcome to Movie Matchmaker! Please follow the prompts below to be matched to your ideal movie! Please make "
          "sure to watch capitalization!\n\nNOTE: We use the data to enter to find the most similar movie across all aspects"
          ", not necessarily the movie that matches everything exactly!")
    while True:

        # userSimilarMovie = input("Enter the movie you want to find something similar to ")
        userFavoriteActors = input("Enter one actor you want to watch today: ")
        userFavoriteGenre = input("Enter your favorite genre: ")
        userPreferredLength = input("Input whether you want a short movie (<90), medium movie (90-120), long (120+): ")
        howManySuggestions = int(input("Input how many suggestions you would like us to generate: "))

        rows = []
        with open("moviedata/movies.csv", 'r') as file:
            reader = csv.reader(file)
            header = next(reader)
            try:
                for row in reader:
                    rows.append(row)
            except UnicodeDecodeError:
                pass

        # Creates the graph and the heap data structure

        # Times the Graph Creation
        a = datetime.now()
        graph = populateGraph(rows)
        b = datetime.now()
        time = b - a
        graphRunningSum += time.total_seconds()


        # Times the Heap Creation
        a = datetime.now()
        movieHeap = populateHeap(rows, Movie("", userFavoriteGenre, userFavoriteActors, userPreferredLength, 10))
        b = datetime.now()
        time = b - a
        heapRunningSum += time.total_seconds()


        # Does the Matchmaking process

        # Times the graph matchmaking process
        print("")
        print("Matchmaking using a graph: \n")
        a = datetime.now()
        matchGraph(graph, userFavoriteGenre, userFavoriteActors, userPreferredLength, howManySuggestions)
        b = datetime.now()
        time = b - a
        graphRunningSum += time.total_seconds()


        # Times the heap matchmaking process
        print("")
        print("Matchmaking using a heap: \n")
        a = datetime.now()
        matchHeap(movieHeap, userFavoriteGenre, userFavoriteActors, userPreferredLength, howManySuggestions)
        b = datetime.now()
        time = b - a
        heapRunningSum += time.total_seconds()


        print("Graph Total Time: " + str(graphRunningSum))
        print("Heap Total Time: " + str(heapRunningSum))
        print("Which was faster? " + "Heap" if heapRunningSum < graphRunningSum else "Graph")

        toExit = input("Press ENTER to continue, any other key to exit: ")
        if toExit != "":
            print("\n\n\nThanks for using Movie MatchMaker!")
            print("--------------------\nCredits: \n")
            print("Chloe Bai\nNora Choukri\nAnna Hudson")
            break



def populateGraph(rows):
    graph = Graph()
    for i in range(len(rows)):  # for all rows of movies
        movie = Movie(rows[i][0], rows[i][2], rows[i][9], rows[i][14], rows[i][5])
        graph.addVertex(movie)
    return graph




def populateHeap(rows, idealMovie):
    heap = Heap()
    for i in range(len(rows)):
        if rows[i][14] == "":
            movie = Movie(rows[i][0], rows[i][2], rows[i][9], -1, rows[i][5])
            if movie.getSimilarity(idealMovie) > 30:
                heap.getArr().append(movie)
        else:
            movie = Movie(rows[i][0], rows[i][2], rows[i][9], rows[i][14], rows[i][5])
            if movie.getSimilarity(idealMovie) > 30:
                heap.getArr().append(movie)
    heap.size = len(heap.getArr())


    temp = Movie(rows[0][0], rows[0][2], rows[0][9], -1, rows[0][5])
    index = 0
    for i in range(0, heap.size):
        if temp.getSimilarity(idealMovie) < heap.getArr()[i].getSimilarity(idealMovie):
            temp = heap.getArr()[i]
            index = i

    heap.heapifyDown(index, idealMovie)
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
    try:
        alreadyPrintedMovies = []
        idealMovie = Movie("", userFavoriteGenre, userFavoriteActors, userPreferredLength, 1000)
        # tempMovie = Movie("", userFavoriteGenre, userFavoriteActors, userPreferredLength, 0)
        highestSim = idealMovie
        heap.getArr().append(idealMovie)
        for movie in heap.getArr():
            if movie.getSimilarity(idealMovie) > highestSim.getSimilarity(idealMovie):
                if movie.movie not in heap.getArr() and movie.getMovie() != idealMovie.movie:
                    highestSim = movie.movie

        heap.heapifyDown(heap.getArr().index(highestSim), idealMovie)
        for i in range(0, int(howManySuggestions)):
            if movie in alreadyPrintedMovies:
                print("No more similar recommendations!")
                break
            else:
                print(heap.extractMax(idealMovie))
                alreadyPrintedMovies.append(heap.extractMax(idealMovie))
    except IndexError:
        print("No more similar recommendations! Check out some of these movies! Happy watching!")



if __name__ == '__main__':
    main()