import csv
import Rating
from Graph import Graph




def main():
    rows = []
    with open("moviedata/movies.csv", 'r') as file:
        reader = csv.reader(file)
        header = next(reader)

        for row in reader:

            rows.append(row)

            try:
                rows.append(row)
            except UnicodeDecodeError:
                pass
           # rating = Rating(row[0], row[1], row[2], row[3])
           # adj_list.insertEdge(rating, rating)



    print(header)
    print(rows)

def welcome():
    print("-----------------------------------")
    print("    Welcome to Movie Matchmaker!   ")
    print("-----------------------------------")
    print("Have you ever wanted to watch a movie but had no idea what to watch, Movie Matchmaker is here to fix this"
          "problem! If you are embroiled in a fight between friends on what movie to watch, we are here to rescue you!")


def menu():
    movie = input("Please enter your favorite movie")
    actor = input("Please enter your favorite actor")
    genre = input("Please enter your favorite genre")

    matchmaker()


def matchmaker():
    # This is where our algorithm for the actual matchmaking process will go
    pass



if __name__ == '__main__':
    main()

