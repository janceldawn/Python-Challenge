#import modules
import os

#import module for reading csv file
import csv

#set the path for file
budget_data_csv = os.path.join('Resources', 'budget_data.csv')

#variables
date = []
profit_losses = []

#Total number of months
#def get_total_months(budget_data_csv):   
total_months = 0

with open(budget_data_csv, 'r') as file:  
    csv_reader = csv.reader(file)
    next(csv_reader)

        #read the header 
        #header = next(csv_reader)

        #loop through the data
    for row in csv_reader:
        total_months +=1

#return total_months
#print statement
print("Financial Analysis")
print("-------------------------------")
print("Total Months:" + " " + str(total_months))

#net total
net_total = 0

with open(budget_data_csv, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)

        for row in csv_reader:
            #try:
                profit_loss = int(row[1]) 
                net_total += profit_loss
            #except ValueError:
                #print(f"Invalid amount on row {csv_reader.line_num}: {row[1]}")

#net_total
#print statement
print("Total:" + " " + "$" + str(net_total))

#changes
#changes = []

#with open(budget_data_csv, 'r') as file:
        #csv_reader = csv.reader(file)
        #next(csv_reader)

        #previous_profit_loss = 0

        #for row in csv_reader:
            #current_profit_loss = int(row[1])
            #change = current_profit_loss - previous_profit_loss
            #changes.append(changes)
            #previous_profit_loss = current_profit_loss

#Average change; len-returns the length of an object
#if len(changes) == 0:   
    #return 0

            #total_changes = sum(changes)
            #average_change = total_changes / len(changes)

#print (f"Average Change:" + str(average_change))

def profit_loss_changes(budget_data_csv):
    changes = []

    with open(budget_data_csv, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)

        previous_profit_loss = 0

        for row in csv_reader:
            try:
                current_profit_loss = int(row[1])
                change = current_profit_loss - previous_profit_loss
                changes.append(change)
                previous_profit_loss = current_profit_loss
            except ValueError:
                print(f"Invalid profit/loss on row {csv_reader.line_num}: {row[1]}")

    return changes

def average_change(changes):
    if len(changes) == 0:
        return 0
    
    total_changes = sum(changes)
    average_change = total_changes / len(changes)
    return average_change

#print(f"Average Change: + str{average_change}")
#(f"Average Change: {average_change}")

print(f"Profit/Loss Changes: {profit_loss_changes}")
print(f"Average Change: {average_change}")




