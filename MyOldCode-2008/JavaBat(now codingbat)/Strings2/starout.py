s=raw_input("\nEnter a string")
i=0
r=""
while(i<len(s)):
	if(i!=0 and i!=len(s)-1):
		if(s[i]!='*' and s[i-1]!='*' and s[i+1]!='*'):
			r=r+s[i]
	elif(i==0):
		if(s[i]!='*' and s[i+1]!='*'):
			r=r+s[i]
	else:
		if(s[i]!='*' and s[i-1]!='*'):
			r=r+s[i]
	i=i+1
print r
raw_input("\nPress enter to finish")		
	


	