import os
import csv

#Create path to csv file
csvpath=os.path.join('..','PyPoll','election_data.csv')

#Creates dictionary to be used for candidate name and vote count
poll = {}

#Create variable for total number of votes
total_votes = 0

#gets data file
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile)

    #skips header line
    next(csvreader, None)

    #creates dictionary from file using column 3, without repeating names
    #counts votes for each candidate
    #counts total votes by counting # of rows without a header 
    for row in csvreader:
        total_votes += 1
        if row[2] in poll.keys():
            poll[row[2]] = poll[row[2]] + 1
        else:
            poll[row[2]] = 1
 
#create empty list vote count of each candidate
candidates = []
num_votes = []

#uses above lists and inputs values, finding candidates and number of votes
for key, value in poll.items():
    candidates.append(key)
    num_votes.append(value)

#find percentage of votes
vote_percent = []
for n in num_votes:
    vote_percent.append(round(n/total_votes*100, 1))

#clean data, put into tuple
new_list = list(zip(candidates, num_votes, vote_percent))

#create a list for the winners
winner_list = []

for name in new_list:
    if max(num_votes) == name[1]:
        winner_list.append(name[0])

# makes winner_list a str with the first entry
winner = winner_list[0]

#prints to file
output_file = os.path.join("..", "PyPoll", "output.txt")

with open(output_file, 'w') as txtfile:
    txtfile.writelines('Election Results \n------------------------- \nTotal Votes: ' + str(total_votes) + 
      '\n-------------------------\n')
    for entry in new_list:
        txtfile.writelines(entry[0] + ": " + str(entry[2]) +'%  (' + str(entry[1]) + ')\n')
    txtfile.writelines('------------------------- \nWinner: ' + winner + '\n-------------------------')

#prints file to terminal
with open(output_file, 'r') as readfile:
    print(readfile.read())