#!/usr/bin/env python
# coding: utf-8


#Import Dependencies
import pandas as pd
import datetime as datetime

#Read the csvfile
df = pd.read_csv("budget_data.csv")

#The total number of months included in the dataset
total_months = df['Date'].nunique()

#The net total amount of "Profit/Losses" over the entire period
net_amount = df['Profit/Losses'].sum()

#The changes in "Profit/Losses" over the entire period, and then the average of those changes
changes = df['Profit/Losses'].diff()
avg_change = changes.mean()

#The greatest increase in profits (date and amount) over the entire period
max_increase = changes.max()
max_date = df.loc[changes.idxmax(), 'Date']

#The greatest decrease in profits (date and amount) over the entire period
max_decrease = changes.min()
min_date = df.loc[changes.idxmin(), 'Date']

#Printing the report
with open("pybank_report.txt", "w") as file:
    file.write("Financial Analysis\n")
    file.write("-"*20 + "\n")
    file.write(f'Total Months: {total_months}\n')
    file.write(f'Total: ${net_amount:,.0f}\n')
    file.write(f'Average Change: ${avg_change:,.2f}\n')
    file.write(f'Greatest Increase in Profits: {max_date} (${max_increase:,.0f})\n')
    file.write(f'Greatest Decrease in Profits: {min_date} (${max_decrease:,.0f})\n')
file.close()

