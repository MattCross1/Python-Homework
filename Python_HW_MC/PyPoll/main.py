#The total number of votes cast
#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote.

import os 
import csv

total_votes = 0
Khan_votes = 0
Correy_votes = 0
Li_votes = 0
Otooley_votes = 0

csvpath = os.path.join('election_data.csv')
with open('election_data.csv') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvfile)

    for row in csvreader:
        total_votes += 1
        if (row[2] == "Khan"):
            Khan_votes += 1
        elif(row[2] == "Correy"):
            Correy_votes += 1
        elif (row[2] == "Li"):
            Li_votes += 1
        else: Otooley_votes += 1


    kahn_percent = Khan_votes / total_votes
    correy_percent = Correy_votes / total_votes
    li_percent = Li_votes / total_votes
    otooley_percent = Otooley_votes / total_votes

    Popular_vote_Winner = max(Khan_votes, Correy_votes, Li_votes, Otooley_votes)

    if Popular_vote_Winner == Khan_votes:
            winner = "Khan"
    elif Popular_vote_Winner == Correy_votes:
            winner = "Correy"
    elif Popular_vote_Winner == Li_votes:
            winner = "Li" 
    else: 
        winner = "OTooley"
          

print(f"Election Results:")
print(f"Total Votes Received: {total_votes}")
print(f"Khan Votes: {kahn_percent:.3%}({Khan_votes})")
print(f"Correy Votes: {correy_percent:.3%}({Correy_votes})")
print(f"Li Votes: {li_percent:.3%}({Li_votes})")     
print(f"O'Tooley Votes: {otooley_percent:.3%}({Otooley_votes})")
print(f"Winner: {winner}!")      


