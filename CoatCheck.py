# This script controls the Coat Check System

#!/usr/bin/env python

import pygtk
pygtk.require("2.0")
import gtk
import gtk.glade
import csv
import serial

csvFile = 'Coats.csv'
Hanger = ''
Name = ''
found = 0

class CoatCheckGTK:

	def __init__(self):
		self.gladefile = "CoatCheckUI.glade"
		self.glade = gtk.Builder()
		self.glade.add_from_file(self.gladefile)
		self.glade.connect_signals(self)
		self.glade.get_object("MainWindow").show_all()		
		
	def on_MainWindow_destroy(self, widget, data=None):
		gtk.main_quit()
		
	def on_btnCheck_clicked(self, widget):
		# Append a new row to csvFile
		with open(csvFile, 'ab') as f:		# open file for appending - 'ab'
			writer = csv.writer(f)
			Name = self.glade.get_object("CheckName").get_text()
			Hanger = self.glade.get_object("CheckNum").get_text()
			writer.writerow([Hanger, Name])
			
			self.glade.get_object("CheckName").set_text('')
			self.glade.get_object("CheckNum").set_text('')
						

	def on_btnRet_clicked(self, widget): #search for input hanger number, print hangernum
		with open(csvFile, 'rb') as f:	 # open file for reading - 'rb'
			#reader = csv.reader(f)
			RetName = self.glade.get_object("RetName").get_text()
			found = 0
			for row in f:
				if row.find(RetName) != -1:
					elementsinrow = row.rsplit(',')
					yummyelement = elementsinrow[1]
					if len(RetName) == (len(yummyelement) -2):
						arduino.write(row[0])
						self.glade.get_object("RetNum").set_text(elementsinrow[0])
						found = 1
					if found == 0:
						self.glade.get_object("RetNum").set_text("*** Did not find name ***")  

	def on_btnEnd_clicked(self, widget):
		arduino.write('E')
		self.glade.get_object("RetName").set_text('')
		self.glade.get_object("RetNum").set_text('')
		#remove from csv		
		#with open(csvFile, 'ab') as f:
		#	writer = csv.writer(f)
		#	for row in f:
		#		if not row[0].startswith("yummyelement"):
		#			writer.writerow(row)
		#		writer.close()
		
if __name__ =="__main__":
	# Connect to Arduino
	try:  
		arduino = serial.Serial('COM3', 9600)
		#self.glade.get_object("ErrorLine").set_text('Connected...')
		print 'Connected...'
	except:  
		print "Failed to connect on COM3" 
		#self.glade.get_object("ErrorLine").set_text("Failed to connect on COM3")
	
	try:
		a = CoatCheckGTK()
		gtk.main()
	except KeyboardInterrupt:
		pass
