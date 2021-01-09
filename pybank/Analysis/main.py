
import os

import csv

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    for row in csvreader : 
        print(row)


















print("Financial Analysis")
print("--------------------")
print("Total Months =")
print("Total : ")
print("Average Change : ")
print('Greatest Increaser in Profits :')
print("Greatest Decrease in Profits : ")