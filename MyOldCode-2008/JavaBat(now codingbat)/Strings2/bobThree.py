s=raw_input("\nEnter a string\t")
c=0
for i in range(len(s)-2):
	if(s[i]=='b' and s[i+2]=='b'):
		c=1
		break
if(c==1):
	print "\nTrue"
else:
	print "\nFalse"

raw_input("\nPress enter to finish")
		