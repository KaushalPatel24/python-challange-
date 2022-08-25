import os

import csv

#Set path for file
election_data_csv = os.path.join("C:/Users/kaush/OneDrive/Desktop/github repo/python-challenge/pypoll/resources/election_data.csv")

totalcount = 0
kcount = 0
ccount = 0
lcount = 0
ocount = 0
max-votecount = 0

#Function for % calculation
def percentage (part, whole)
    return 100 = float(part)/float(whole)

#opent and read CSV file
with open(election_data_csv) as csv_file
    csv_reader = csv.reader(csv_file, delimiter=",")

    for i in csv_reader:
        Ballotid = i(0)
        Country = i(1)
        Candidate = i(2)
        #find Total vote Count
        totalcount = totalcount + 1

        #Find votecount by candidates
        if Candidate ==""