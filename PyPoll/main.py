#import modules
import os

#import module for reading csv file
import csv

#set the path for file
election_data_csv = os.path.join('Resources', 'election_data.csv')

#variables
ballot_ID= []
county = []
candidate =[]

#set total number of votes, candidate votes, vote percentage
total_number_votes = 0
candidates = set ()
candidate_votes = {}
total_votes = 0
vote_percentages = {}


with open(election_data_csv, 'r') as file:  
    csv_reader = csv.reader(file)
    next(csv_reader) #read the header


        #loop through the data
    for row in csv_reader:
        total_number_votes +=1
        candidate = row[2] #candidate is 2, since it's 3rd column and starts at 0
        candidates.add(candidate)

        candidate = row[2] 
        total_votes += 1

        #getting vote for each candidate
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1

#getting max number of votes and matching with the candidate
winner = max(candidate_votes, key=candidate_votes.get)
total_votes = sum(candidate_votes.values())


#print statement of the output
print("Election Results")
print("------------------------------------")
print("Total Votes:" + " " + str(total_number_votes))
print("------------------------------------")


#print("Candidates who received votes:")
#for candidate in candidates:
    #print(candidate)


#print("Total Votes per Candidate:")
#for candidate, votes in candidate_votes.items():
    #print(f"{candidate}: {votes} votes")

#print("\nVote Percentages:")
for candidate, votes in candidate_votes.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")

print("-----------------------------------")
print(f"Winner: {winner}")
print("-----------------------------------")

