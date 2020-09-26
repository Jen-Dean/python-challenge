import os
import csv

from datetime import datetime

Em_ID = []

FirstName = []
LastName = []

Month = []
Day = []
Year = []
BirthDate = []

SSNumber_1 = []
SSNumber_2 = []
SSNumber_3 = []

State = []

SplitName = 0
Birthday = 0
Raw_SSN = 0
dob = 0

#join the file information to read from
data_csv = os.path.join("/Users/jenniferdean/Desktop/DATA_SCIENCE_BOOTCAMP/GitHub/HOMEWORK/python-challenge/PyBoss/Resources/employee_data.csv")

with open(data_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csv_reader)

#Create a Loop to place all Variables into the proper lists
    for row in csv_reader:
        Em_ID.append(row[0])

        #The Name column should be split into separate First Name and Last Name columns.
        SplitName = row[1].split(" ")
        FirstName.append(SplitName[0])
        LastName.append(SplitName[1])

        ############Birthday = row[2].split("-")
        ############Year.append(Birthday[0])
        ############Month.append(Birthday[1])
        ############Day.append(Birthday[2])

        #The DOB data should be re-written into MM/DD/YYYY format.
        date_time_object = datetime.strptime(row[2], '%Y-%m-%d')
        dob = date_time_object.strftime('%m/%d/%Y')
        BirthDate.append(dob)

        #The SSN data should be re-written such that the first five numbers are hidden from view.
        Raw_SSN = row[3].split("-")
        SSNumber_1.append(Raw_SSN[0])
        SSNumber_2.append(Raw_SSN[1])
        SSNumber_3.append(Raw_SSN[2])
        
        




        #The State data should be re-written as simple two-letter abbreviations.
        State.append(row[4])


SSNumber_1() = "***"
#SSNumber_1[1] = "***"
#SSNumber_1[2] = "***"

#for row in SSNumber_1:
    #row = SSNumber_1 = "***"



print(SSNumber_1)

#SSNumber_1[0:2] = "***"

#print(SSNumber_1)





#Merge the List and Export into a csv