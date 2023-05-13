import csv

# Open the CSV file and read it
with open('budget_data.csv') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # skip the header row

    # Initialize variables
    total_months = 0
    net_amount = 0
    previous_profit_loss = 0
    changes = []

    # Loop through the rows
    for row in csv_reader:
        # Count the number of months
        total_months += 1

        # Calculate the net amount
        net_amount += int(row[1])

        # Calculate the change in profit/losses
        if previous_profit_loss != 0:
            change = int(row[1]) - previous_profit_loss
            changes.append(change)
        previous_profit_loss = int(row[1])

    # Calculate the average change
    avg_change = sum(changes) / len(changes)

    # Find the greatest increase and decrease in profit/losses
    max_change = max(changes)
    min_change = min(changes)

    # Find the months with the greatest increase and decrease in profit/losses
    with open('budget_data.csv') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # skip the header row
        for row in csv_reader:
            if int(row[1]) - previous_profit_loss == max_change:
                max_month = row[0]
            if int(row[1]) - previous_profit_loss == min_change:
                min_month = row[0]
            previous_profit_loss = int(row[1])

# Print the report
print("Financial Analysis")
print("-"*20)
print(f"Total Months: {total_months}")
print(f"Total: ${net_amount}")
print(f"Average Change: ${round(avg_change, 2)}")
print(f"Greatest Increase in Profits: {max_month} (${max_change})")
print(f"Greatest Decrease in Profits: {min_month} (${min_change})")
