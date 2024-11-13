# -*- coding: UTF-8 -*-

# Dependencies
import csv
import os
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Set file paths for budget and output files 
inputfile = os.path.join("Resources", "budget_data.csv")
outputfile = os.path.join("analysis", "budget_analysis.txt")

# Define variables to track total months and the total net
total_months = 0
total_net = 0 # profit / losses
total_chg = 0 # cumlative change

# Define variables to track the greatest and least changes
lastmn_profit = 0
currmn_profit = 0
lastcurr_change = 0
change_max = 0
change_least = 0
month_max = 0
month_least = 0

# Budget Data file (Open and read)
with open(inputfile) as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')

    #Reads the first row
    csv_header = next(csvreader) 

    # Process each row of data after the header row
    for row in csvreader:

         # print(row)
        total_months += 1
        total_net += int(row[1])

        # check if first row - skip first row
        if total_months == 1:
            lastmn_profit = int(row[1])
        else:
            # get the current month's profit / loss and calculate the change
            currmn_profit = int(row[1])
            change = currmn_profit - lastmn_profit
            total_chg += change

            
            # Track the greatest increase and decrease
            if change > change_max:
                change_max = change
                month_max = row[0]
                
            if change < change_least:
                change_least = change
                month_least = row[0]

        # Update last month's profit for the next iteration
            lastmn_profit = currmn_profit
            
# Calculate average change
avg_change = total_chg / (total_months - 1)

# Generate output summary
output = f"""
Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${total_net:}
Average Change: ${avg_change:.2f}
Greatest Increase in Profits: {month_max} (${change_max:})
Greatest Decrease in Profits: {month_least} (${change_least:})
"""

# Print output summary to the terminal
print(output)

# Write the results to a text file
with open(outputfile, "w") as txt_file:
    txt_file.write(output)