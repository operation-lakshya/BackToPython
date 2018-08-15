s=raw_input("\nEnter a string")
def parenBit(s):
	n=len(s)
	if(n==0):
		return ""
	elif(s[0]=='('):
		if(s[n-1]==')'):
			return s[0:n]
		else:
			return parenBit(s[:(n-1)])
	else:
		return parenBit(s[1:])
print parenBit(s)