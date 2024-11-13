# -*- coding: UTF-8 -*-

# Dependencies
import csv
import os
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Define paths for input and output files (ensure correct paths)
input_file = os.path.join("Resources/election_data.csv")
output_file = os.path.join("Analysis_election_data_analysis.txt")

# Track the total number of votes cast
total_votes = 0

# Define a dictionary to track candidate names and vote counts
vote_dict = {}

# Winning Candidate and Winning Count Tracker
candidate_winner = ""
max_votes_per_candidate = 0

# Open the CSV file and process it
with open(input_file) as election_data:
    reader = csv.reader(election_data)

    # Skip header row and start at the first row
    header = next(reader)

    # Keep track of votes for each candidate
    for row in reader:

        # Print a loading indicator (for large datasets)
        print(". ", end="")

        # Increment the total vote count for each row
        total_votes += 1

        # Get the candidate's name from the row (3rd column in CSV)
        candidate = row[2]

        # Add a vote to the candidate's count or initialize if new candidate
        vote_dict[candidate] = vote_dict.get(candidate, 0) + 1

# Generate the output summary
print(vote_dict)
output = f"""
Election Results
-------------------------

Total Votes: {total_votes}

-------------------------
"""

# Loop through the dictionary to calculate percentages and determine the winner
for candidate, votes in vote_dict.items():
    vote_percent = round(100 * votes / total_votes, 3)

    # Check if we have a new winner
    if votes > max_votes_per_candidate:
        max_votes_per_candidate = votes
        candidate_winner = candidate

    # Add candidate results to the output string
    output += f"{candidate}: {vote_percent}% ({votes})\n"

# Add the winner to the output
output += f"""-------------------------

Winner: {candidate_winner}

-------------------------
"""

# Print the output to the console
print(output)

# Write the results to the output file
with open(output_file, "w") as txt_file:
    txt_file.write(output)
