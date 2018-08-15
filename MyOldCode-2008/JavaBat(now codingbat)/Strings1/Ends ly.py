s=raw_input("\nEnter a string:\t")
if ((s[len(s)-1]=='y' and s[len(s)-2]=='l') or (s[len(s)-1]=='Y' and s[len(s)-2]=='L') ):
	print "\nTrue"
else:
	print "\nFalse"

raw_input("\nPress enter to finish")