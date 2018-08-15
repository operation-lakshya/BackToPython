choice = 0
while choice<1:
	s=raw_input("\nEnter a string")
	i=0
	r=""
	
	while(i<len(s)):
		if(s[i]=='z' and s[i+2]=='p'):
			r=r+s[i]+s[i+2]
			i=i+2
		else:
			r=r+s[i]
		i=i+1
	print r
	
	
	choice = input("\nDo u want to continue press 0 to continue or enter 1 to exit")

		