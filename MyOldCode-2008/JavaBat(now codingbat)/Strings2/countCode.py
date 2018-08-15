s=raw_input("\nEnter a string\t")
count=0
for i in range(len(s)-3):
	if(s[i]=='c' and s[i+1]=='o' and s[i+3]=='e'):
		count=count+1
print count
raw_input("\nPress enter to finish")
		