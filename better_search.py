def on_btnRet_clicked(self, widget): #search for input hanger number, print hangernum
	with open(csvFile, 'rb') as f:	 # open file for reading - 'rb'
		#reader = csv.reader(f)
		RetName = self.glade.get_object("RetName").get_text()
		found = 0
		for row in f:	
			if row.find(RetName) != -1:
				elementsinrow = row.split(",")
				yummyelement = elementsinrow[1]
					if len(RetName) == len(yummyelement):
						arduino.write(row[0])
						print RetName + "'s coat on Hanger", row[0]
						found = 1
					if found == 0:
						print "*** Did not find name ***" 
# that should work for getting it to search and compare the lengths to make sure they are the same
#Justin things that the print commande for the UI will be something like glade.this_space().print, 