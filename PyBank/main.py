#Import Needed Modules
import os
import csv

#State the Variables Needed
MonthCount = 0
NetRevenue = 0
MaxRevenue = 0
MinRevenue = 0
AvgRevenue = 0

#Create Lists to Store the CSV Data in Python
Month = []
Revenue = []

#Zip the lists together to keep the data paired
Zipped = zip(Month, Revenue)

#join the file information to read from
budget_csv = os.path.join("/Users/jenniferdean/Desktop/DATA_SCIENCE_BOOTCAMP/GitHub/HOMEWORK/python-challenge/PyBank/Resources/budget_data.csv")
with open(budget_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    
    #Remove the Header from the document
    csv_header = next(csv_reader)

    #Create the Loop to go through all the rows:
    for row in csv_reader:
        #Count the total rows in column 0 (MonthCount)
        MonthCount += 1
        #Add the integers to a database in Python [Revenue]
        Revenue.append(int(row[1]))
        #Add the Months to a database in Python [Month]
        Month.append(str(row[0]))
        #Zipper the Data Together so you can pull the information later
        Zipped = zip(Month, Revenue)

#Get the total, min and max of the integers in the list
NetRevenue = sum(Revenue)
AvgRevenue = round((sum(Revenue)/len(Revenue)), 2)
MaxRevenue = max(Revenue)
MinRevenue = min(Revenue)

#find the month row and with the Max/Min and print
for row in Zipped:
    if row[1] == MaxRevenue:
        MaxRevMonth = str(f"{row[0]}, {MaxRevenue}")    
    if row[1] == MinRevenue:
        MinRevMonth = str(f"{row[0]}, {MinRevenue}")

#Print the Results
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {MonthCount}")
print(f"Total: {NetRevenue}")
print(f"Average Change: {AvgRevenue}")
print(f"Greatest Increase in Profits: {MaxRevMonth}")
print(f"Greatest Decrease in Profits: {MinRevMonth}")

        