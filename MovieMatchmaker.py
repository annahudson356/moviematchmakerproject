import csv
import Graph
import Heap
import Movie


def main():
    '''
    userFavoriteActor = input("Enter the actor you want to watch today, if not type 0")
    userFavoriteGenre = input("Enter your favorite genre")
    userPreferredLength = input("Input whether you want a short movie (<90), medium movie (90-120), long (120+) ")
    howManySuggestions = input("Input how many suggestions you would like us to generate")
    '''

    rows = []
    with open("moviedata/movies.csv", 'r') as file:
        reader = csv.reader(file)
        header = next(reader)
        try:
            for row in reader:
                rows.append(row)
        except UnicodeDecodeError:
            pass

    print(header)
    print(rows, end='\n')

def populateGraph(rows, userFavoriteGenre, userFavoriteActor, userPreferredLength):
    graph = Graph.Graph()
    idealMovie = Movie.Movie("", userFavoriteGenre, userFavoriteActor, userPreferredLength, 10)
    for row in rows:
        movie = Movie.Movie(row[0], row[2], row[9], row[14],row[5]) # someone can double check i added the correct attributes according to dataset lol
        graph.addVertex(movie) # adds the movie AND adds edges to any similar existing movies (see graph class)



def matchmaker(rows):
    # This is where our algorithm for the actual matchmaking process will go
    pass


if __name__ == '__main__':
    main()

