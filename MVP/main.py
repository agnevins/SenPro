# Amanda Nevins 
# Senior Project 487 Spring 2018
# MVP Soroity Sort 

# Citings:
# latin-1: https://stackoverflow.com/questions/39001641/unicodedecodeerror-on-python3
# https://www.sitepoint.com/using-python-parse-spreadsheet-data/
# https://pythonspot.com/files-spreadsheets-csv/
# https://docs.python.org/2/library/csv.html#csv.DictReader
# https://docs.python.org/3/library/index.html
# https://stackoverflow.com/questions/15129567/csv-writer-writing-each-character-of-word-in-separate-column-cell
# https://code.tutsplus.com/tutorials/how-to-read-and-write-csv-files-in-python--cms-29907

# PLAN OF ACTION, Greek Day Seating chart:
# Create a sorted "rush" list based on (in order)
#   1. Legacy status 
#   2. Points
#   3. State*
#   4. Group number (for output excel)

import csv
rush = list(csv.DictReader(open("rush2.csv","r",encoding='utf-8', errors='ignore')))

for row in rush:
    print(row)
    print(row["Total"])
    row["Total"] = int(row["Total"])
    if row["Legacy"] == 'Yes':
        row["Total"] += 50

rush = sorted(rush, key= lambda x: x['Total'], reverse=True)

# Sort by state


# Dynamic list of the group numbers 

groups = [[] for x in range(12)]
for row in rush:
	groups[int(row['Group #'])-1].append(row)

print(groups)




# Create output excel file of sorted women
myFile = open('CHART.csv', 'w')

with myFile:
    writer = csv.writer(myFile, delimiter=",", dialect="excel", lineterminator="\n")
    writer.writerow(["Table","Seat", "Name","Group #"])

    #table = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

    # Retrieve only Names for Seating Chart
    #count = 0
    for x in groups:
        count = 0
        writer.writerow("\n")
        number = 1
        table = 1
        for y in x:
            writer.writerow([(count//8)+1]+[number]+[y['First Name'] + " " + y['Last Name']] +[y['Group #']])
            if number != 8:
                number += 1
            else:
                number = 1
            count += 1




# Need tables to be 8 = 1 , then 8 = 2, ... etc.



# [(count//8)+1]






