# Import dependencies
import os 
import csv

# Assign file location
csv_file = os.path.join('Desktop','Data Analytics Boot Camp','3.0 Python','python-challenge', 'PyPoll', 'election_data.csv')

# Declare Variables 
total_votes = 0 
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0

# Open csv
with open(csv_file,newline="", encoding="utf-8") as elections:

    # Split the data on commas
    csvreader = csv.reader(elections,delimiter=",") 

    # Next the header labels
    header = next(csvreader)     

    # Loop through each row in the csv
    for row in csvreader: 

        # Count the unique Voter ID's and store in variable called total_votes
        total_votes +=1

        # Count the times candidate's name appears and store in list
        if row[2] == "Khan": 
            khan_votes +=1
        elif row[2] == "Correy":
            correy_votes +=1
        elif row[2] == "Li": 
            li_votes +=1
        elif row[2] == "O'Tooley":
            otooley_votes +=1

# Make a dictionary out of the two lists 
candidates = ["Khan", "Correy", "Li", "O'Tooley"]
votes = [khan_votes, correy_votes, li_votes, otooley_votes]

# Return the winner using a max function of the dictionary 
dict_candidates_and_votes = dict(zip(candidates,votes))
key = max(dict_candidates_and_votes, key=dict_candidates_and_votes.get)

# Summary of the analysis
khan_percent = (khan_votes/total_votes) *100
correy_percent = (correy_votes/total_votes) * 100
li_percent = (li_votes/total_votes)* 100
otooley_percent = (otooley_votes/total_votes) * 100

# Print statements
print(f"Election Results")
print(f"--------------------------")
print(f"Total Votes: {total_votes}")
print(f"--------------------------")
print(f"Khan: {khan_percent:.3f}% ({khan_votes})")
print(f"Correy: {correy_percent:.3f}% ({correy_votes})")
print(f"Li: {li_percent:.3f}% ({li_votes})")
print(f"O'Tooley: {otooley_percent:.3f}% ({otooley_votes})")
print(f"--------------------------")
print(f"Winner: {key}")
print(f"--------------------------")

# Output file
output_file = os.path.join('Desktop','Data Analytics Boot Camp','3.0 Python','python-challenge', 'PyPoll', 'Election_Results.txt')

with open(output_file,"w") as file:

    # Write Elections_Results.txt
    file.write(f"Election Results")
    file.write("\n")
    file.write(f"--------------------------")
    file.write("\n")
    file.write(f"Total Votes: {total_votes}")
    file.write("\n")
    file.write(f"--------------------------")
    file.write("\n")
    file.write(f"Khan: {khan_percent:.3f}% ({khan_votes})")
    file.write("\n")
    file.write(f"Correy: {correy_percent:.3f}% ({correy_votes})")
    file.write("\n")
    file.write(f"Li: {li_percent:.3f}% ({li_votes})")
    file.write("\n")
    file.write(f"O'Tooley: {otooley_percent:.3f}% ({otooley_votes})")
    file.write("\n")
    file.write(f"--------------------------")
    file.write("\n")
    file.write(f"Winner: {key}")
    file.write("\n")
    file.write(f"--------------------------")
    