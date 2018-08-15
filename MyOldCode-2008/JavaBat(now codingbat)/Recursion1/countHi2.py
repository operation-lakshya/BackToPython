s=raw_input("\nEnter a string")
def countHi2(s):
	if(len(s)<2):
		return 0
	elif(s[0]=='x'):
		return countHi2(s[2:])
	elif(s[:2]=="hi"):
		return 1+countHi2(s[2:])
	else:
		return countHi2(s[1:])
print countHi2(s)