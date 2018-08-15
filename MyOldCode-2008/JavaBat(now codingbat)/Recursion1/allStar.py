s=raw_input("\nEnter a string:\t")
def allStar(s):
	l=len(s)
	if(l==1):
		return s[l-1]
	else:
		return allStar(s[:(l-1)])+"*"+s[l-1]
print allStar(s)