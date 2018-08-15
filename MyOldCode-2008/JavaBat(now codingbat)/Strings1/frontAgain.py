a=raw_input("\nEnter a string\t")
if (len(a)<2):
	print "\nThere are less than two characters"
elif (a[:2]==a[-2:]):
	print "\nTrue"
else:
	print "\nFalse"

raw_input("\nPress enter to finish")