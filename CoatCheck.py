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
		with open(csvFile, 'rb') as f:		# open file for reading - 'rb'
			#reader = csv.reader(f)
			RetName = self.glade.get_object("RetName").get_text()
			found = 0
			for row in f:						
				if row.find (RetName) != -1:
					arduino.write(row[0])
					print RetName + "'s coat on Hanger", row[0]
					found = 1
			if found == 0:
				print "*** Did not find name ***" 

	def on_btnEnd_clicked(self, widget):
		arduino.write('E')
		self.glade.get_object("RetName").set_text('')
		
if __name__ =="__main__":
	# Connect to Arduino
	try:  
		arduino = serial.Serial('COM3', 9600)
		print 'Connected...'
	except:  
		print "Failed to connect on COM3" 
	
	try:
		a = CoatCheckGTK()
		gtk.main()
	except KeyboardInterrupt:
		pass