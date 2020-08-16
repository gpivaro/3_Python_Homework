import csv


# Relative path for the dataset csv file
file_path = "PyPoll/Resources/Homework_03-Python_Instructions_PyPoll_Resources_election_data.csv"
output_file_path = "PyPoll/analysis/elections.txt"

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
# The total number of votes cast
total_number_votes = len(voter_ID)


# A complete list of candidates who received votes
# Use set function to retrieve unique values
list_candidates = list(set(candidate))


# The total number of votes each candidate won
total_number_votes_candidate = []
for name in list_candidates:
    num_vote = 0
    for vote in candidate:
        if vote == name:
            num_vote += 1
    total_number_votes_candidate.append(num_vote)


# The percentage of votes each candidate won
percentage_votes_candidate_won = [
    (vote / total_number_votes) * 100 for vote in total_number_votes_candidate
]


# The winner of the election based on popular vote.
winner = 0
j = 0
for cand_vote in percentage_votes_candidate_won:
    if cand_vote > winner:
        winner = cand_vote
        winner_index = j
    j += 1
winner_election = list_candidates[winner_index]


print()
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_number_votes:,.0f}")
print("-------------------------")

for i in range(len(list_candidates)):
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

    for i in range(len(list_candidates)):
        text.write(
            f"{list_candidates[i]} {percentage_votes_candidate_won[i]:,.2f}% ({total_number_votes_candidate[i]:,.0f})\n"
        )

    text.write("-------------------------\n")
    text.write(f"{winner_election}\n")
    text.write("-------------------------\n")
