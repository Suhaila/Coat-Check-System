# This script controls the Coat Check System

#!/usr/bin/env python

import pygtk
pygtk.require("2.0")
import gtk
import gtk.glade
import csv
import serial
import pango

csvFile = 'Coats.csv'
buffer = 'buffer.csv'
Hanger = ''
Name = ''
found = 0

class CoatCheckGTK:

	def __init__(self):
		self.gladefile = "CoatCheckUI2.glade"
		self.glade = gtk.Builder()
		self.glade.add_from_file(self.gladefile)
		self.glade.connect_signals(self)
		self.glade.get_object("MainWindow").show_all()
		
	def on_MainWindow_destroy(self, widget, data=None):
		gtk.main_quit()
	
	def on_entry_activate(self, widget):
		widget.get_toplevel().child_focus(gtk.DIR_TAB_FORWARD)
	def on_entry_CheckName(self, widget):
		self.glade.get_object("CheckNum").grab_focus()
	def on_entry_CheckNum(self, widget):# this doesn't appear to work here
		self.glade.get_object("btnCheck").grab_focus()
	def on_entry_RetName(self, widget):
		self.glade.get_object("btnRet").grab_focus()
	def on_entry_HangerNum(self, widget):# this doesn't appear to work here
		self.glade.get_object("btnEnd").grab_focus()
	
	def on_btnCheck_clicked(self, widget):
		# Append a new row to csvFile
		with open(csvFile, 'ab') as f:		# open file for appending - 'ab'
			writer = csv.writer(f)
			Name = self.glade.get_object("CheckName").get_text()
			Hanger = self.glade.get_object("CheckNum").get_text()
			writer.writerow([Hanger, Name])
			# Clear contents
			self.glade.get_object("CheckName").set_text('')
			self.glade.get_object("CheckNum").set_text('')
			# Move focus to Name field
			self.glade.get_object("CheckName").grab_focus()
			#show what is stored
			self.glade.get_object("CheckDetails").set_text(Name + ' is on hanger ' + Hanger)

	def on_btnRet_clicked(self, widget): #search for input hanger number, print hangernum
		with open(csvFile, 'rb') as f:	 # open file for reading - 'rb'
			RetName = self.glade.get_object("RetName").get_text()
			found = 0
			for row in f:
				if row.find(RetName) != -1:
					elementsinrow = row.rsplit(',')
					yummyelement = elementsinrow[1]
					if len(RetName) == (len(yummyelement) -2):
						arduino.write(elementsinrow[0])
						self.glade.get_object("RetNum").set_text(RetName + "'s coat is on hanger # "+ elementsinrow[0])
						found = 1
					if found == 0:
						self.glade.get_object("RetNum").set_text("*** Did not find name ***")
				if found == 0:
						self.glade.get_object("RetNum").set_text("*** Did not find name ***")
		self.glade.get_object("HangerNum").grab_focus() 	 

	def on_btnEnd_clicked(self, widget):
		
		HangerNum = self.glade.get_object("HangerNum").get_text()
		
		with open(csvFile, 'rb') as f:	 # open file for reading - 'rb'
			RetName = self.glade.get_object("RetName").get_text()
			found = 0
			for row in f:
				if row.find(RetName) != -1:
					elementsinrow = row.rsplit(',')
					yummyelement = elementsinrow[1]
					if len(RetName) == (len(yummyelement) -2):
						found = 1
						hangernumber = elementsinrow[0]
					if found == 0:
						self.glade.get_object("RetNum").set_text("*** Did not find name ***")
				if found == 0:
						self.glade.get_object("RetNum").set_text("*** Did not find name ***")
				
			self.glade.get_object("RetName").set_text('')
			self.glade.get_object("RetName").grab_focus()
		
		if HangerNum == hangernumber: #if the scanned hanger and number in system match, remove it
			#remove from csv		
			with open(csvFile, 'rb') as f:
				with open(buffer, 'wb') as b:
					writer = csv.writer(b)
					for row in f:
						elementsinrow = row.rsplit(',')
						if not elementsinrow[0].startswith(hangernumber):
							b.write(row) 
			with open(csvFile, 'wb') as f:
				with open(buffer, 'rb') as b:
					for row in b:
						f.write(row)
		
			self.glade.get_object("RetName").set_text('')
			self.glade.get_object("HangerNum").set_text('')
			self.glade.get_object("RetNum").set_text('Scan Customer ID')
		
			arduino.write('E')
			# pull 
		
		else: #hanger numbers don't match 
			self.glade.get_object("RetNum").set_text('This is not the correct hanger, find hanger ' + HangerNum + ' please try again.')
			self.glade.get_object("HangerNum").set_text('')
			
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
