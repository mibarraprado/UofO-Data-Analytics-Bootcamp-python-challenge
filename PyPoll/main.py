#import os and csv modules to read data on the csv files
import os
import csv

#variables to store data
Total_votes=0
votes_per_candidate =0
votes_per_candidate_percentage=0.000
unique_candidates = []
candidate_votes= []
candidate_votes_percentage = []
poll= []
#getting path to the current directory where main.py file is stored
current_directory = os.getcwd()
#path to the data file  
csvpath = os.path.join(current_directory, "Resources", "election_data.csv")
#path to the output file
outputfile = os.path.join(current_directory,"analysis", "election_data_analysis.txt")

#defining a function to count candidates votes. This function takes a list named votes where all votes are stored and the name of the candidate
#this function returns the number of votes
def countvotes(votes, x):
    votes_per_candidate = 0
    for item in votes:
        if (item == x):
            votes_per_candidate = votes_per_candidate+1
    return votes_per_candidate

#open CSV file where poll data is stored
with open(csvpath, encoding='utf') as csvfile:
    #read csv file
    csvreader = csv.reader(csvfile, delimiter=",")
    #read header
    csv_header = next(csvfile)
    
    #for loop to read data rows in the csv file
    for row in csvreader:
            #store all the votes in a list named poll. Stores the name of the candidate that receives the votes
            poll.append(str(row[2]))
            #count total votes. One for each row 
            Total_votes = Total_votes + 1
            #check if a candidate has been stored in the unique_candidate list, if not it will be added to the list
            if str(row[2]) not in unique_candidates:
                unique_candidates.append(str(row[2]))

    # for loop to count the votes that eanch candidate received by calling the countvotes function. 
    # The votes of the candidates are stored in the  candidates_votes list and votes_per_candidate_percentage
    for candidate in unique_candidates:
        candidate_votes.append(countvotes(poll,candidate))
        votes_per_candidate_percentage = round(countvotes(poll,candidate)/Total_votes *100,3)
        candidate_votes_percentage.append(votes_per_candidate_percentage)

# Find the candidate with the max votes and get the index  with in the list. 
# This index will be used get the name of the candidate winning the elecction
maxindex=candidate_votes_percentage.index(max(candidate_votes_percentage))

#generate the output list that contains the election results. Each item in the list is a line that will written in the output file
output = ["Election Results \n",
    "----------------------------\n", 
    f"Total Votes: {Total_votes}\n", 
    "----------------------------\n"]
#For loop to generate the lines in the file that contain data votes for each candidate    
for j in range(len(unique_candidates)):
    output.append(f"{unique_candidates[j]}: {candidate_votes_percentage[j]}% ({candidate_votes[j]})\n")
#addng the last lines to the output list
output.append("----------------------------\n")
output.append(f"Winner: {unique_candidates[maxindex]}\n")
output.append("----------------------------\n")

# write output file
with open(outputfile,"w") as analysis:
    for line in output:
        analysis.write(line)
          