s=raw_input("Enter the string")
def countAbc(s):
	if(len(s)<3):
		return 0
	elif(s[:3]=="abc" or s[:3]=="aba"):
		return 1+countAbc(s[3:])
	else:
		return countAbc(s[1:])
print countAbc(s)
