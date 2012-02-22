# This is the main script for our Coat Check System
# Read the README for how to run the script :)

# importing modules to be used in the script
import csv 
import serial

# define some variables
csvFile = 'Sample_data.csv'

# Opens the csvFile, reads the data, and prints it on the screen
with open(csvFile, "rb") as file:
	reader = csv.reader(file)
	for row in reader:		# for loop to read each row in the file
		print row

# Append a new row to csvFile (hardcoded for now until we get input from a barcode scanner) 
with open(csvFile, 'ab') as f:		# open file for appending - 'ab'
    writer = csv.writer(f)
    writer.writerow([004, 'Alex', 'Mann', 456789012])

