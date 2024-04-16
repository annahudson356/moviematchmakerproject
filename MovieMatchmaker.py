import pandas as p
import csv

def main():
    rows = []
    with open("resources/Movie Data/ratings_export.csv", 'r') as file:
        csvreader = csv.reader(file)
        header = next(csvreader)
        for row in csvreader:
            rows.append(row)
    print(header)
    print(rows)






if __name__ == '__main__':
    main()



