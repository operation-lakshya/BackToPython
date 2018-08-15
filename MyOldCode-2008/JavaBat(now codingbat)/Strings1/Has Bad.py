s=raw_input("\nEnter a string:\t")
if ((s[:3]=="bad" or s[1:4]=="bad") or (s[:3]=="BAD" or s[1:4]=="BAD")):
	print "\nTrue"
else:
	print "\nFalse"
raw_input("\nPress enter to finish")