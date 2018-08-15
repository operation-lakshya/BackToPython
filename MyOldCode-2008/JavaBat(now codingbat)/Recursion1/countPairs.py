s=raw_input("Enter the string")
def countPairs(s):
	if(len(s)<3):
		return 0
	elif(s[0]==s[2]):
		return 1+countPairs(s[1:])
	else:
		return countPairs(s[1:])
print countPairs(s)
