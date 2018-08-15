s=raw_input("\nEnter a string:\t")
def endX(s):
	if(len(s)==0):
		return ""
	elif(s[0]=='x'):
		return endX(s[1:])+'x'
	else:
		return s[0]+endX(s[1:])
print endX(s)
