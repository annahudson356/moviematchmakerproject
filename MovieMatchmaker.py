import csv
import Graph
import Heap

def main():
    userFavoriteActor = input("Enter the actor you want to watch today, if not type 0")
    userFavoriteGenre = input("Enter your favorite genre")
    userPreferredLength = input("Input whether you want a short movie (<90), medium movie (90-120), long (120+) ")
    howManySuggestions = input("Input how many suggestions you would like us to generate")



    rows = []
    with open("moviedata/movies.csv", 'r') as file:
        reader = csv.reader(file)
        header = next(reader)
        try:
            for row in reader:

                rows.append(Movie(row[0], row[1], row[2], row[3]))
        except UnicodeDecodeError:
            pass



    print(header)
    print(rows)


def matchmaker():
    # This is where our algorithm for the actual matchmaking process will go
    pass



if __name__ == '__main__':
    main()

