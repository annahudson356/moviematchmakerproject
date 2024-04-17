import pandas as p
import csv
import itertools
import threading
import time
import sys



def main():
    rows = []

    with open("moviedata/Movie Data/ratings_export.csv", 'r') as file:
        reader = csv.reader(file)
        header = next(reader)
        for row in reader:
            rows.append(row)


    print(header)
    print(rows)




if __name__ == '__main__':
    main()



