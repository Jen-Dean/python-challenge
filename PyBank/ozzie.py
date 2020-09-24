import os
import csv
import statistics

total_months = []
total_profits = []

average_Change = []
greatest_Increase = []
greatest_Decrease = []
monthly_profit_margin = []
net_change = 0

csvpath = os.path.join("/Users/jenniferdean/Desktop/DATA_SCIENCE_BOOTCAMP/GitHub/HOMEWORK/python-challenge/PyBank/Resources/budget_data.csv")
#print(csvpath)

with open(csvpath) as budget_data:
    csvreader = csv.reader(budget_data, delimiter=",")

#print(budget_data)

    header = next(csvreader)
    firstrow = next(csvreader)

    rowbefore = (int(firstrow[1]))

    print(rowbefore)

    total_months.append(firstrow[0])

    total_profits.append(int(firstrow[1]))

    rowbefore = (int(firstrow[1]))

# Loop loopp loooop pa dooooo

    for row in csvreader:
        total_months.append(row[0])
        total_profits.append(int(row[1]))
        net_change = int(row[1]) - rowbefore
        rowbefore = int(row[1])
        #print(rowbefore)
        monthly_profit_margin.append(net_change)
        #print(net_change)
        # 
print(monthly_profit_margin)
