s=raw_input("\nEnter a string")
t=raw_input("\nEnter a string")
i=0
b=""
while(i<len(s) and i<len(t)):
	b=b+s[i]+t[i]
	i=i+1
if(i<len(s)):
	b=b+s[i:]
if(i<len(t)):
	b=b+t[i:]
print "\nOutput is: ",b
raw_input("\nPres enter to finish")
	