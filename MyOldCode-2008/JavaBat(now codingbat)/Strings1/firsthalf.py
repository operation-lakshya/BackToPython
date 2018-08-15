s=raw_input("\nEnter a string of even length:\t")
if (len(s)%2!=0):
	print "\nSory,youhave to enter an even length string"
print s[:len(s)/2]
raw_input("\nPress enter to finish")