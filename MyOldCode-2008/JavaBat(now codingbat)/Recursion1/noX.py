s=raw_input("\nEnter the string:\t")
def noX(s):
	l=len(s)
	if(l==0):
		return ""
	elif(s[l-1]=='x'):
		return noX(s[:(l-1)])
	else:
		return noX(s[:(l-1)])+s[l-1]
print noX(s)