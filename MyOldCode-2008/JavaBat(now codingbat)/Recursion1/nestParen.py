s=raw_input("\nEnter a string")
f=1
def nestParen(s):
	global f
	n=len(s)
	if(n==0):
		return f	
 	elif(s[0]=='('):
		if(len(s)==1):
			f=1
			return f
		elif(s[n-1]==')'):
			f=0
			return nestParen(s[1:(n-1)])
		else:
			return nestParen(s[:(n-1)])
	else:
		return nestParen(s[1:])
if(nestParen(s)==0):
	print "\nTrue"
else:
	print "\nFalse"
