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
    print(rows)

    graph = Graph.Graph()
    for i in range(len(rows)-1):  # for all rows of movies
        for j in range(len(rows[0])):  # for all attributes of movies
            a = Movie.Movie(rows[i][j])  # two temporary movie objects
            b = Movie.Movie(rows[i+1][j])
        graph.insertEdge(a, b)  # insert edge between movie objects

def matchmaker():
    # This is where our algorithm for the actual matchmaking process will go
    pass

if __name__ == '__main__':
    main()

