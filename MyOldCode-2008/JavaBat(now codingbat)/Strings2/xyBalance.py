s=raw_input("\nEnter a string\t")
i=0
if(len(s)==0):
	print "\nyou are given an empty string"
else:
	r=""
	while(i<len(s)):
		if(s[i]=='x'):
			r="false"
		if(s[i]=='y'):
			r="true"
		i=i+1
	if(r=="false"):
		print "\nFalse"
	else:
		print "\nTrue"
raw_input("\nPress enter to finish")