s=raw_input("\nEnter the string:\t")
def changeXY(s):
	l=len(s)
	if(l==0):
		return ""
	elif(s[l-1]=='x'):
		return changeXY(s[:(l-1)])+'y'
	else:
		return changeXY(s[:(l-1)])+s[l-1]
		
print changeXY(s)