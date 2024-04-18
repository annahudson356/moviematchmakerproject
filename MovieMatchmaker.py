# import pandas as p
import csv
import itertools
import threading
import time
import sys
import Rating
from Graph import Graph




def main():
    # adj_list = Graph()
    rows = []
    with open("moviedata/movies.csv", 'r') as file:
        reader = csv.reader(file)
        header = next(reader)

        for row in reader:
            try:
                rows.append(row)
            except UnicodeDecodeError:
                pass
           # rating = Rating(row[0], row[1], row[2], row[3])
           # adj_list.insertEdge(rating, rating)



    print(header)
    print(rows)






if __name__ == '__main__':
    main()



