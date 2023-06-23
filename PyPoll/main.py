#import modules
import os

#import module for reading csv file
import csv

#set the path for file
election_data_csv = os.path.join('Resources', 'election_data.csv')

#set total number of votes, candidate votes, vote percentage
total_number_votes = 0
candidate_lists = set ()
candidate_list_votes = {}
max_votes = 0
winner = None


with open(election_data_csv, 'r') as file:  
    csv_reader = csv.reader(file, delimiter=",")
    
    #header
    next(csv_reader)

    #loop through the data
    for row in csv_reader:
        total_number_votes +=1
        candidate_list = row[2] #candidate_list is 2, since it's 3rd column and starts at 0
        candidate_lists.add(candidate_list)


        #getting vote for each candidate_list
        if candidate_list in candidate_list_votes:
            candidate_list_votes[candidate_list] += 1
        else:
            candidate_list_votes[candidate_list] = 1


#print statement of the output
print("Election Results")
print("------------------------------------")
print("Total Votes:" + " " + f"{total_number_votes}")
print("------------------------------------")

for candidate_list, votes in candidate_list_votes.items():
    percentage = (votes / total_number_votes) * 100

    print(f"{candidate_list}: {percentage:.3f}% ({votes})")

    if votes > max_votes:
        max_votes = votes
        winner = candidate_list


print("-----------------------------------")
print(f"Winner: {winner}")
print("-----------------------------------")

#output path
output_path = os.path.join("analysis", "analysis.txt")

with open(output_path, 'w') as analysis:
    analysis.write("Election Results\n\n")
    analysis.write("-------------------------------\n\n")
    analysis.write("Total Votes:" + " " + f"{total_number_votes}\n\n")
    analysis.write("-------------------------------\n\n")

    for candidate_list, votes in candidate_list_votes.items():
        percentage = (votes / total_number_votes) * 100

        analysis.write(f"{candidate_list}: {percentage:.3f}% ({votes})\n\n")

        if votes > max_votes:
            max_votes = votes
            winner = candidate_list

    analysis.write("-------------------------------\n\n")
    analysis.write(f"Winner: {winner}\n\n")
    analysis.write("-------------------------------\n\n")