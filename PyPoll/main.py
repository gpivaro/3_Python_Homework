import csv
import os

# Use os library to retrieve the base directory of this file
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Using the os library to import the dataset file
file_path = os.path.join(
    BASE_DIR,
    "PyPoll",
    "Resources",
    "Homework_03-Python_Instructions_PyPoll_Resources_election_data.csv",
)
output_file_path = os.path.join(BASE_DIR, "PyPoll", "analysis", "elections.txt")


# Create empty lists to store the data from the csv file
voter_ID = []
county = []
candidate = []

# open and read the csv file
with open(file_path, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    header = next(csvreader)
    # print(header)

    for row in csvreader:
        voter_ID.append(row[0])
        county.append(row[1])
        candidate.append(row[2])


# Analyzes the votes and calculates each of the following:

# -------------------------------------------------------------
# 1. The total number of votes cast
# -------------------------------------------------------------
total_number_votes = len(voter_ID)


# A complete list of candidates who received votes
# Use set function to retrieve unique values
list_candidates = list(set(candidate))

# -------------------------------------------------------------
# 2. The total number of votes each candidate won
# -------------------------------------------------------------
total_number_votes_candidate = []
for name in list_candidates:
    num_vote = 0
    for vote in candidate:
        if vote == name:
            num_vote += 1
    total_number_votes_candidate.append(num_vote)

# -------------------------------------------------------------
# 3. The percentage of votes each candidate won
# -------------------------------------------------------------
percentage_votes_candidate_won = [
    (vote / total_number_votes) * 100 for vote in total_number_votes_candidate
]


# Order the list of percentage of votes
percentage_votes_ordered = sorted(percentage_votes_candidate_won, reverse=True)

# Retrieve the index of the sorted percentage in the original list of votes
winner_index = []
for votes_order in percentage_votes_ordered:
    j = 0  # Initialize the variable that will retrieve the index
    for perc_votes in percentage_votes_candidate_won:
        if perc_votes == votes_order:
            get_index = j
        j += 1
    winner_index.append(get_index)

# -------------------------------------------------------------
# 4. The winner of the election based on popular vote.
# -------------------------------------------------------------
winner_election = list_candidates[winner_index[0]]


# Print the results in the terminal
print()
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_number_votes:,.0f}")
print("-------------------------")
for i in winner_index:
    print(
        f"{list_candidates[i]} {percentage_votes_candidate_won[i]:,.2f}% ({total_number_votes_candidate[i]:,.0f})"
    )
print("-------------------------")
print(winner_election)
print("-------------------------")


# Save the result to a text file
with open(output_file_path, "w") as text:
    text.write("Election Results\n")
    text.write("-------------------------\n")
    text.write(f"Total Votes: {total_number_votes:,.0f}\n")
    text.write("-------------------------\n")

    for i in winner_index:
        text.write(
            f"{list_candidates[i]} {percentage_votes_candidate_won[i]:,.2f}% ({total_number_votes_candidate[i]:,.0f})\n"
        )

    text.write("-------------------------\n")
    text.write(f"{winner_election}\n")
    text.write("-------------------------\n")

print()
print(f"Results saved to:\n{output_file_path}")

