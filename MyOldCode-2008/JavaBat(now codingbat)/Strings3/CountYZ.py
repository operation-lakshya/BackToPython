s=raw_input("\nEnter the string")
i=0
count = 0
while(i<len(s)):
	if(s[i]=='y' or s[i]=='Y' or s[i]=='z' or s[i]=='Z'):
		if(i==len(s)-1 or s[i+1]==" "):
			count = count+1
	i=i+1
print count 