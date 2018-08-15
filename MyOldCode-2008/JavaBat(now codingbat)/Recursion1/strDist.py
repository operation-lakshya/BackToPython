s=raw_input("\nEnter a string")
t=raw_input("\nenter a substring in the given string")
def strDist(s,t):
	n=len(s)
	if(n==0):
		return 0
	elif(s[:len(t)]==t):
		if(s[(-len(t)):]==t):
			return len(s[0:n])
		else:
			return strDist(s[:(n-1)],t)
	else:
		return strDist(s[1:],t)
print strDist(s,t)