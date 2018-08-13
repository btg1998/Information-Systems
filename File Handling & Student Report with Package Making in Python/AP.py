import csv
import json
import sys
from operator import itemgetter

def accept_input(Data,DI):
    with open('final.csv', 'r') as csvfile:
        read = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in read:
            Data.append(row)
        print("Data:")
        for i in Data:
            print(i)
    return(Data,DI)
