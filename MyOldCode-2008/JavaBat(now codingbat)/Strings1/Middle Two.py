s=raw_input("\nEnter a string of even length:\t")
if (len(s)%2!=0):
	print "\nIt is an odd length string so not possible to take middle ones"
if (len(s)==2):
	print "\nIt is a 2 characters string so there is no middle one"
else:
	print s[len(s)/2-1]+s[len(s)/2]
	
raw_input("\nPress enter to finish")