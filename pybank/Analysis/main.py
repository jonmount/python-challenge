
import os

import csv

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')




total_months = 0 
sum_profits = 0 

change = 0 
previous = 0 


monthly_profits = []

great_inc_date = []
great_dec_date = []




with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    
    print(csvreader)

    next(csvreader)

    for row in csvreader : 

        total_months = total_months + 1 

        sum_profits = sum_profits+ int(row[1])

        

       
        if total_months > 1 : 
            change = int(row[1]) - previous 
            

            monthly_profits.append(change)

            previous = int(row[1])

         



            



           




average = sum(monthly_profits)/ (total_months - 1)

great_prof_inc = max(monthly_profits)
great_prof_dec = min(monthly_profits)

print("Financial Analysis")
print("--------------------")
print(f"Total Months : {total_months}")
print(f"Total : {sum_profits}")
print(f"Average Change : {round(average, 2)}")
print(f'Greatest Increase in Profits : {great_prof_inc}')
print(f'Greatest Decrease in Profits :  {great_prof_dec}')


with open("pybank_output.txt", "w") as txt_file: 
    txt_file.write("Financial Analysis\n")
    txt_file.write("--------------------\n")
    txt_file.write(f"Total Months : {total_months}\n")
    txt_file.write(f"Total : {sum_profits}\n")
    txt_file.write(f"Average Change : {average}\n")
    txt_file.write(f'Greatest Increase in Profits : {great_prof_inc}\n')
    txt_file.write(f'Greatest Decrease in Profits :  {great_prof_dec}\n')


