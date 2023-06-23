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

# PyPoll

# The following code was based on Lesson Plans, Python Challenge, Activities. This code imports and reads the csv file.

## code
#import modules
import os

#import module for reading csv file
import csv

#set the path for file
election_data_csv = os.path.join('Resources', 'election_data.csv')

# This code based on PyBank listing and storing data.

## code
#set total number of votes, candidate votes, vote percentage
total_number_votes = 0
candidate_lists = set ()
candidate_list_votes = {}
max_votes = 0
winner = None

# The following code was based on Lesson Plans, Python Challenge, Activities. This code imports and reads csv file and setting the for loop.

## code
with open(election_data_csv, 'r') as file:  
    csv_reader = csv.reader(file, delimiter=",")
    
    #header
    next(csv_reader)

# This code snippet based from PyBank. This code assigns the total number of votes counter to keep track of total number of votes, and the candidates list dictionary to store number of votes each candidate has received. 

## code

    #loop through the data
    for row in csv_reader:
        total_number_votes +=1
        candidate_list = row[2] #candidate_list is 2, since it's 3rd column and starts at 0
        candidate_lists.add(candidate_list)

# The following code snippet from Chat GPT. In the for loop, the code goes through each row of the file, it increase the total number of votes by 1 and checks if that candidate is already in candidate list votes dictionary. If candidate already in the dictionary, then their vote is increased/added by 1, but if candidate is new, candidate is added to the dictionary with the initial vote of 1.

## code

        #getting vote for each candidate_list
        if candidate_list in candidate_list_votes:
            candidate_list_votes[candidate_list] += 1
        else:
            candidate_list_votes[candidate_list] = 1

# The following code was based on Lesson Plans, Python Challenge, Activities. The code prints the results to the terminal, also include using f-string.

## code

#print statement of the output to terminal
print("Election Results")
print("------------------------------------")
print("Total Votes:" + " " + f"{total_number_votes}")
print("------------------------------------")

for candidate_list, votes in candidate_list_votes.items():
    percentage = (votes / total_number_votes) * 100

    print(f"{candidate_list}: {percentage:.3f}% ({votes})")

# The following code based on Stack Overflow - 'using max to find highest in the list'. This code looks for the maximum number of votes and also candidate with the maximum number of votes in the loop. The code then matches the current candidate votes to the maximum number of votes.

    if votes > max_votes:
        max_votes = votes
        winner = candidate_list


print("-----------------------------------")
print(f"Winner: {winner}")
print("-----------------------------------")

# The following code was based on PyBank, exproting results into text file.

## code

#output path
output_path = os.path.join("analysis", "analysis.txt")

with open(output_path, 'w') as analysis:
    analysis.write("Election Results\n\n")
    analysis.write("-------------------------------\n\n")
    analysis.write("Total Votes:" + " " + f"{total_number_votes}\n\n")
    analysis.write("-------------------------------\n\n")

# The following code snippet for exporting results to text file, for loop section, guidance by AskBCs LA Mohamed. The code loops through the candidate list and print every candidate to text file.

## code, for loop section

    for candidate_list, votes in candidate_list_votes.items():
        percentage = (votes / total_number_votes) * 100

        analysis.write(f"{candidate_list}: {percentage:.3f}% ({votes})\n\n")

        if votes > max_votes:
            max_votes = votes
            winner = candidate_list

    analysis.write("-------------------------------\n\n")
    analysis.write(f"Winner: {winner}\n\n")
    analysis.write("-------------------------------\n\n")