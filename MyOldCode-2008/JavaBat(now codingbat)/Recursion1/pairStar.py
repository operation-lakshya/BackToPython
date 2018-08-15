s=raw_input("\nEnter a string:\t")
def pairStar(s):
	l=len(s)
	if(l==1):
		return s[l-1]
	elif(s[l-2]==s[l-1]):
		return pairStar(s[:(l-1)])+"*"+s[l-1]
	else:
		return pairStar(s[:(l-1)])+s[l-1]
print pairStar(s)