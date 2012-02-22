# This is the main script for our Coat Check System

import csv # imports the 'csv' module so that you can use it

csvFile = 'Sample_data.csv' # defines the csv file with the data

with open(csvFile, "rb") as file:
	reader = csv.reader(file)
	for row in reader:
		print row

 
with open(csvFile, 'ab') as f:
    writer = csv.writer(f)
    writer.writerow([004, 'Alex', 'Mann', 456789012])

