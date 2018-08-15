s=raw_input("\nEnter a string")
i=0
c=0
while(i<len(s)):
	if(s[i]=='*'):
		if(i!=0 and i!=len(s)-1):
			if(s[i-1]==s[i+1]):
				c=1
			else:
				c=0
	
	i=i+1
if(c==1):
	print "\nTrue"
else:	
	print "\nFalse"
raw_input("\nPress enter to finish")