import os
import csv


TotalVotes = 0

VoterIDList = []
CountyList = []
CandidateList = []

KhanCount = 0
CorreyCount = 0
LiCount = 0
OTooleyCount = 0

Winner = "jenniferdean"

election_csv = os.path.join("/Users/jenniferdean/Desktop/DATA_SCIENCE_BOOTCAMP/GitHub/HOMEWORK/python-challenge/PyPoll/Resources/election_data.csv")
with open(election_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    #Remove the Header from the document
    csv_header = next(csv_reader)

    #Create the Loop to go through the rows
    for row in csv_reader:
            #The total number of votes cast
            TotalVotes += 1
            VoterIDList.append(str(row[0]))
            #A complete list of candidates who received votes
            CandidateList.append(str(row[2]))

#The total number of votes each candidate won
KhanCount = CandidateList.count("Khan")
CorreyCount = CandidateList.count("Correy")
LiCount = CandidateList.count("Li")
OTooleyCount = CandidateList.count("O'Tooley")

#The winner of the election based on popular vote.
CanVoteList = [KhanCount, CorreyCount, LiCount, OTooleyCount]

if (max(CanVoteList)) == KhanCount:
    Winner = "Khan"
elif max(CanVoteList) == CorreyCount:
    Winner = "Correy"
elif max(CanVoteList) == LiCount:
    Winner = "Li"
else:
    Winner = "O'Tooley"


print("Election Results")
print("-------------------------")
print(f"Total Votes: {TotalVotes}")
print(f"Khan: %%% ({KhanCount})")
print(f"Correy: %%% ({CorreyCount})")
print(f"Li: %%% ({LiCount})")
print(f"O'Tooley: %%% ({OTooleyCount})")
print(f"Winner: {Winner}")

#zipper = zip(VoterIDList, CandidateList)






#The percentage of votes each candidate won



