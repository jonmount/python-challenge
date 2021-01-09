
import os

import csv

csvpath = os.path.join('..', 'Resources', 'election_data.csv')


total_votes = 0 


candidate_list = []

candidate_dictionary = {}




with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    
    print(csvreader)

    next(csvreader)

    for row in csvreader : 

        total_votes = total_votes + 1

        candidate = row[2]

        if candidate in candidate_list : 

            candidate_dictionary[candidate] = candidate_dictionary[candidate] +1 

        
        else :
            candidate_list.append(candidate)
            candidate_dictionary[candidate] = 1
            





print("-------------------------")
print(f'Total Votes: {total_votes}')
print("-------------------------")
for candidate, vote_count in candidate_dictionary.items() : 
    print(f"{candidate} + {vote_count}")
print("-------------------------")
print("Winner: ")
print("-------------------------")