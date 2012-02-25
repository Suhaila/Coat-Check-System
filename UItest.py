#!/usr/bin/env python

#second attempt at getting something from Glade to run in python, so I can make pretty things

import pygtk
pygtk.require("2.0")
import gtk
import gtk.glade

class CoatCheckGTK:

	def __init__(self):
		self.gladefile = "CoatCheckUI.glade"
		self.glade = gtk.Builder()
		self.glade.add_from_file(self.gladefile)
		self.glade.connect_signals(self)
		self.glade.get_object("MainWindow").show_all()
		
	def on_MainWindow_destroy(self, widget, data=None):
		gtk.main_quit()
		
	def on_btnHelloWorld_clicked(self, widget):
		print "Hello World!"
		
if __name__ =="__main__":
	try:
		a = CoatCheckGTK()
		gtk.main()
	except KeyboardInterrupt:
		pass