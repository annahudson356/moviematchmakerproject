import pandas as p
import csv
import itertools
import threading
import time
import sys
import Rating
import Graph



def main():
    adj_list = Graph()
    rows = []
    with open("moviedata/Movie Data/ratings_export.csv", 'r') as file:
        reader = csv.reader(file)
        header = next(reader)
        for row in reader:
            rows.append(row)
            rating = Rating(row[0], row[1], row[2], row[3])
            adj_list.insertEdge(rating, rating)



    print(header)
    print(rows)






if __name__ == '__main__':
    main()



