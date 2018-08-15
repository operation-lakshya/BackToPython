s=raw_input("\nEnter the string:\t")
def changePi(s):
	l=len(s)
	if(l==0):
		return ""
	elif(s[l-2:]=='pi'):
		return changePi(s[:(l-2)])+'3.14'
	else:
		return changePi(s[:(l-1)])+s[l-1]
		
print changePi(s)