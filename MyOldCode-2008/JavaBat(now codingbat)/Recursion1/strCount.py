s=raw_input("\nEnter a string")
t=raw_input("\nEnter a sub string to count in the given string")
def strCount(s,t):
	if(len(s)<len(t)):
		return 0
	elif(s[:len(t)]==t):
		return 1+strCount(s[len(t):],t)
	else:
		return strCount(s[1:],t)
print strCount(s,t)
	