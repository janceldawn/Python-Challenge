# Python-Challenge

# PyBank

# The following code was based on Lesson Plans, Python Challenge, Activities. This code imports and reads the csv file.

## code
#import modules
import os

#import module for reading csv file
import csv

#set the path for file
budget_data_csv = os.path.join('Resources', 'budget_data.csv')

# Listing and storing data guided by ASKBCs LA. Needed clarification on when to use 0, None, [].

#list and store data
total_months = 0
net_total = 0
profit_changes = []
dates = []
previous_profit_change = None
greatest_increase = 0
greatest_decrease = 0
increase_date = None
decrease_date = None

# The following code was based on Lesson Plans, Python Challenge, Activities. This code imports and reads csv file and setting the for loop.

## code

#open and read csv file 
with open(budget_data_csv, 'r') as file:
    csv_reader = csv.reader(file, delimiter=",")
    
    #header
    next(csv_reader)

    for row in csv_reader:
        total_months +=1
        date = row[0] #column in csv file
        profit_change = int(row[1]) #for column in csv file
        net_total += profit_change
        
        dates.append(date)

 # The following code snippet from Chat GPT. The code goes through the rows and calculate the changes in profit/loss and calculates the change by subtracting previous profit change from the current profit change. These changes are stored in profit_changes list. Average change is calculated by dividing the sum of the profit_changes by the number of profit_changes.

 ## code

        if previous_profit_change is not None:
            change = profit_change - previous_profit_change
            profit_changes.append(change)

# The following code snippet and guidance provided by AskBCs LA. The code checks if current change is greater than current greatest increase or lesser than current greatest decrease. It matches specific greatest increase or decrease to a date.

## code

            if change > greatest_increase:
                greatest_increase = change
                increase_date = date

            if change < greatest_decrease:
                greatest_decrease = change
                decrease_date = date

        previous_profit_change = profit_change

average_change = sum(profit_changes) / len(profit_changes)

# The following code was based on Lesson Plans, Python Challenge, Activities. The code prints the results to the terminal, also include using f-string.

## code

#print statement
print("Financial Analysis")
print("-------------------------------")
print("Total Months:" + " " + f"{total_months}")
print("Total:" + " " + " " + f"${net_total}")
print("Average change:" + " " + f"${average_change:.2f}")
print("Greatest Increase in Profits:" + " " + increase_date + " " + f"(${greatest_increase})")
print("Greatest Decrease in Profits:" + " " + decrease_date + " " + f"(${greatest_decrease})")

# The following code snippet and guidance provided by AskBCs LA Ryan. The following code exports and print the output of the terminal into a text file.

## code
#output path
output_path = os.path.join("analysis", "analysis.txt")

with open(output_path, 'w') as analysis:
    analysis.write("Financial Analysis\n\n")
    analysis.write("-------------------------------\n\n")
    analysis.write("Total Months:" + " " + f"{total_months}\n\n")
    analysis.write("Total:" + " " + f"${net_total}\n\n")
    analysis.write("Average change:" + " " + f"${average_change:.2f}\n\n")
    analysis.write("Greatest Increase in Profits:" + " " + increase_date + " " + f"(${greatest_increase})\n\n")
    analysis.write("Greatest Decrease in Profits:" + " " + decrease_date + " " + f"(${greatest_decrease})\n\n")
