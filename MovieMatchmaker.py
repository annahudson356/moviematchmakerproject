import csv
from datetime import datetime
from Graph import Graph
from Heap import Heap
from Movie import Movie




def main():
    graphRunningSum = 0
    heapRunningSum = 0
    print("Welcome to Movie Matchmaker! Please follow the prompts below to be matched to your ideal movie! Please make "
          "sure to watch capitalization and spelling!\n\nNOTE: We use the data to enter to find the most similar movie across all aspects"
          ", not necessarily the movie that matches everything exactly!\n")
    while True:
        toExit = input("Press ENTER to continue, any other key to exit: ")
        if toExit != "":
            print("\nThanks for using Movie MatchMaker!")
            print("--------------------\nCredits: \n")
            print("Chloe Bai\nNora Choukri\nAnna Hudson")
            break

        # gathers input for preferred movie
        userFavoriteActors = input("Enter one actor you want to watch today: ")
        userFavoriteGenre = input("Enter your favorite genre: ")
        userMovieAge = input("Input whether you want an old movie (before 2000s) or new movie (after 2000s): ")
        userPreferredLength = input("Input whether you want a short movie (<90), medium movie (90-120), long (120+): ")
        howManySuggestions = int(input("Input how many suggestions you would like us to generate: "))

        rows = []
        with open("moviedata/movies.csv", 'r') as file: # pass the movie data into rows
            reader = csv.reader(file)
            header = next(reader)
            try:
                for row in reader:
                    rows.append(row)
            except UnicodeDecodeError:
                pass


        # times the graph creation
        a = datetime.now()
        graph = populateGraph(rows)
        b = datetime.now()
        time = b - a
        graphRunningSum += time.total_seconds()




        # times the heap creation
        a = datetime.now()
        movieHeap = populateHeap(rows, Movie("", userFavoriteGenre, userFavoriteActors, userMovieAge, userPreferredLength, 10))
        b = datetime.now()
        time = b - a
        heapRunningSum += time.total_seconds()


        # does the Matchmaking process

        # times the graph matchmaking process
        print("")
        print("Matchmaking using a graph: \n")
        a = datetime.now()
        matchGraph(graph, userFavoriteGenre, userFavoriteActors, userMovieAge, userPreferredLength, howManySuggestions)
        b = datetime.now()
        time = b - a
        graphRunningSum += time.total_seconds()


        # times the heap matchmaking process
        print("")
        print("Matchmaking using a heap: \n")
        a = datetime.now()
        matchHeap(movieHeap, userFavoriteGenre, userFavoriteActors, userMovieAge, userPreferredLength, howManySuggestions)
        b = datetime.now()
        time = b - a
        heapRunningSum += time.total_seconds()


        # compares which data structure was faster
        print("Graph Total Time: " + str(graphRunningSum))
        print("Heap Total Time: " + str(heapRunningSum))
        print("Which was faster? " + "Heap" if heapRunningSum < graphRunningSum else "Graph")
        print()


def populateGraph(rows): # populates the graph with each movie in the dataset
    graph = Graph()
    for i in range(len(rows)):  # for all rows of movies
        movie = Movie(rows[i][0], rows[i][2], rows[i][9], rows[i][3], rows[i][14], rows[i][5])
        graph.addVertex(movie) # adds the vertex and edges to all similar movies
    return graph

def matchGraph(graph, userFavoriteGenre, userFavoriteActors, userMovieAge, userPreferredLength, howManySuggestions):
    idealMovie = Movie("", userFavoriteGenre, userFavoriteActors, userMovieAge, userPreferredLength, 10) # creates ideal movie to compare to
    graph.addVertex(idealMovie) # adds the ideal movie to the graph and edges to its similar movies
    movies = graph.getEdges(idealMovie)
    movie_list = []
    # adds the movies with the highest similarity to the ideal movie for how many suggestions user wants
    while len(movie_list) < howManySuggestions:
        top = None
        highestSim = 0
        for movie in movies:
            if movie.getSimilarity(idealMovie) > highestSim:
                if movie not in movie_list and movie.movie != idealMovie.movie:
                    highestSim = movie.getSimilarity(idealMovie)
                    top = movie
        movie_list.append(top)
    # sorts the movies so that movies with the same similarity score will be ranked highest to lowest based of their rating
    sorted_movies = sorted(movie_list, key=lambda movie: (movie.getSimilarity(idealMovie), movie.getScore()), reverse=True)
    for movie in sorted_movies:
        print(movie.getMovie() + " - Rating: " + movie.getScore() + "/10 - Similarity Score: " + str(movie.getSimilarity(idealMovie)) + "/20")




def populateHeap(rows, idealMovie):
    heap = Heap()
    for i in range(len(rows)): # adds each movie in the dataset to the max heap
        movie = Movie(rows[i][0], rows[i][2], rows[i][9], rows[i][3], rows[i][14], rows[i][5])
        heap.getArr().append(movie)
        heap.size = heap.size + 1
        heap.heapifyUp(i, idealMovie)
    return heap


def matchHeap(heap, userFavoriteGenre, userFavoriteActors, userMovieAge, userPreferredLength, howManySuggestions):
    idealMovie = Movie("", userFavoriteGenre, userFavoriteActors, userMovieAge, userPreferredLength, 1000)
    movie_list = []
    while (len(movie_list) < howManySuggestions): # extract this max and add to movie_list for number of suggestions user inputted
        movie_list.append(heap.extractMax(idealMovie))
    # sorts the movies so that movies with the same similarity score will be ranked highest to lowest based of their rating
    sorted_movies = sorted(movie_list, key=lambda movie: (movie.getSimilarity(idealMovie), movie.getScore()),reverse=True)
    for movie in sorted_movies:
        print(movie.getMovie() + " - Rating: " + movie.getScore() + "/10 - Similarity Score: " + str(movie.getSimilarity(idealMovie)) + "/20")
    print()


if __name__ == '__main__':
    main()