
import os

import csv

csvpath = os.path.join('..', 'Resources', 'election_data.csv')


total_votes = 0 





with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    
    print(csvreader)

    next(csvreader)

    for row in csvreader : 

        total_votes = total_votes + 1



print("-------------------------")
print(f'Total Votes: {total_votes}')
print("-------------------------")
print("Put votes for each candidate here")
print("-------------------------")
print("Winner: ")
print("-------------------------")