
import os

import csv

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')




total_months = 0 
sum_profits = 0 


with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    
    print(csvreader)

    next(csvreader)

    for row in csvreader : 

        total_months = total_months + 1 

        sum_profits = sum_profits+ int(row[1])

        
       
















print("Financial Analysis")
print("--------------------")
print(f"Total Months : {total_months}")
print(f"Total : {sum_profits}")
print("Average Change : ")
print('Greatest Increaser in Profits :')
print("Greatest Decrease in Profits : ")