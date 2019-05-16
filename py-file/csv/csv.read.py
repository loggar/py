import csv

filename = "my_data.csv"

fields = []
rows = []

# Reading csv file
with open(filename, 'r') as csvfile:
    # Creating a csv reader object
    csvreader = csv.reader(csvfile)

    # Extracting field names in the first row
    fields = csvreader.next()

    # Extracting each data row one by one
    for row in csvreader:
        rows.append(row)

# Printing out the first 5 rows
for row in rows[:5]:
    print(row)
