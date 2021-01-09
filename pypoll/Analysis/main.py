
import os

import csv

csvpath = os.path.join('..', 'Resources', 'election_data.csv')


total_votes = 0 


candidate_list = []

candidate_dictionary = {}

max_vote = 0 




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
            

  




with open("pypoll_output.txt", "w") as txt_file: 
    txt_file.write("Election Results\n")
    txt_file.write("-------------------------\n")
    txt_file.write(f"Total Votes : {total_votes}\n")
    txt_file.write("-------------------------\n")

    print("-------------------------")
    print(f'Total Votes: {total_votes}')
    print("-------------------------")
    for candidate, vote_count in candidate_dictionary.items() : 
        percent = float(candidate_dictionary[candidate]) / float(total_votes) 
        percent = round(percent * 100, 2)
        print(f"{candidate} : {percent} % {vote_count} \n")

        num_votes =candidate_dictionary[candidate] 
        winning_vote = candidate 
        if num_votes >  max_vote  :
        
            max_vote = num_votes 
            winner = candidate 
    print("-------------------------")
    print(f'Winner: {winner}')
    print("-------------------------")



    for candidate, vote_count in candidate_dictionary.items() : 
        txt_file.write(f"{candidate} : {percent} % {vote_count}\n")
    txt_file.write("-------------------------\n")
    txt_file.write(f'Winner: {winner}\n')
    txt_file.write("-------------------------\n'")