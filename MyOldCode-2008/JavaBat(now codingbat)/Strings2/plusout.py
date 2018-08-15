s=raw_input("\nEnter a string")
w=raw_input("\nEnter a non empty word")
i=0
r=""
while(i<len(s)):
	if(s[i:i+len(w)]==w):
		r=r+w
		i=i+len(w)-1
	else:
		r=r+'+'
	i=i+1
	
print r
raw_input("\nPress enter to finish")		
	


	