a=raw_input("\nEnter a string\t")
if (len(a)<2):
	print "\nThere are less than two characters"

elif ((a[len(a)-1] in a[:2]) and (a[len(a)-2] in a[:2])):
	print "\nTrue"
else:
	print "\nFalse"

raw_input("\nPress enter to finish")