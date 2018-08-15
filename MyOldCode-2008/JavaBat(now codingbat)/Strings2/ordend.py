s=raw_input("\nEnter a string")
w=raw_input("\nEnter a non empty word")
i=0
r=""
while(i<len(s)):
	if(i+len(w)<=len(s)):
		if(s[i:(i+len(w))]==w):
			if(i!=0):
				if(i+len(w)<len(s)):
					r=r+s[i-1]+s[i+len(w)]
					i=i+len(w)-1
				else:
					r=r+s[i-1]
					i=i+len(w)-1
			else:
				r=r+s[i+len(w)]
				i=i+len(w)-1
	
	i=i+1
	
print r
raw_input("\nPress enter to finish")		
	


	