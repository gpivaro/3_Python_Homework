import csv
import os

# -------------------------------------------------------------
# Use os library to retrieve the base directory of this file
# -------------------------------------------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# -------------------------------------------------------------
# Using the os library to import the dataset file
# -------------------------------------------------------------
file_path = os.path.join(
    BASE_DIR,
    "PyBank",
    "Resources",
    "Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv",
)
output_file_path = os.path.join(
    BASE_DIR, "PyBank", "analysis", "Financial_Analysis.txt"
)

# -------------------------------------------------------------
# Create the empty list for the dataset
# -------------------------------------------------------------
date = []
Profit_Losses = []

# Open and read the dataset file
with open(file_path, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    header = next(csvreader)

    for row in csvreader:
        date.append(row[0])
        Profit_Losses.append(int(row[1]))

# -------------------------------------------------------------
# 1. The total number of months included in the dataset
# -------------------------------------------------------------
total_number_months = len(date)

# -------------------------------------------------------------
# 2. The net total amount of "Profit/Losses" over the entire period
# -------------------------------------------------------------
total_amount_Profit_Losses = sum(Profit_Losses)

# -------------------------------------------------------------
# 3. The average of the changes in "Profit/Losses" over the entire period
# -------------------------------------------------------------
changes = []
for i in range(len(Profit_Losses) - 1):
    changes.append(Profit_Losses[i + 1] - Profit_Losses[i])
average_changes_Profit_Losses = sum(changes) / (total_number_months - 1)

# -------------------------------------------------------------
# 4. The greatest increase in profits (date and amount) over the entire period
# -------------------------------------------------------------
greatest_increase_profits = 0
for i in range(len(Profit_Losses)):
    if Profit_Losses[i] - Profit_Losses[i - 1] > greatest_increase_profits:
        greatest_increase_profits = Profit_Losses[i] - Profit_Losses[i - 1]
        date_greatest_increase_profits = date[i]

# -------------------------------------------------------------
# 5. The greatest decrease in losses (date and amount) over the entire period
# -------------------------------------------------------------
greatest_decrease_losses = 0
for i in range(len(Profit_Losses)):
    if Profit_Losses[i] - Profit_Losses[i - 1] < greatest_decrease_losses:
        greatest_decrease_losses = Profit_Losses[i] - Profit_Losses[i - 1]
        date_greatest_decrease_losses = date[i]


# -------------------------------------------------------------
# Print the final results in the terminal
# -------------------------------------------------------------
print()
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_number_months}")
print(f"Total ${total_amount_Profit_Losses:,.0f}".replace("$-", "-$"))
print(f"Average Change ${average_changes_Profit_Losses:,.0f}".replace("$-", "-$"))
print(
    f"Greatest Increase in Profits: {date_greatest_increase_profits} (${greatest_increase_profits:,.0f})".replace(
        "$-", "-$"
    )
)
print(
    f"Greatest Decrease in Profits: {date_greatest_decrease_losses} (${greatest_decrease_losses:,.0f})".replace(
        "$-", "-$"
    )
)

# -------------------------------------------------------------
# Save the result to a text file
# -------------------------------------------------------------
with open(output_file_path, "w") as text:
    text.write("Financial Analysis\n")
    text.write("----------------------------\n")
    text.write(f"Total Months: {total_number_months}\n")
    text.write(f"Total ${total_amount_Profit_Losses:,.0f}\n".replace("$-", "-$"))
    text.write(
        f"Average Change ${average_changes_Profit_Losses:,.0f}\n".replace("$-", "-$")
    )
    text.write(
        f"Greatest Increase in Profits: {date_greatest_increase_profits} (${greatest_increase_profits:,.0f})\n".replace(
            "$-", "-$"
        )
    )
    text.write(
        f"Greatest Decrease in Profits: {date_greatest_decrease_losses} (${greatest_decrease_losses:,.0f})\n".replace(
            "$-", "-$"
        )
    )
print()
print("-------------------------")
print(f"Results saved to:\n{output_file_path}")
