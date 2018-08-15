s=raw_input("\nEnter a string")
def count11(s):
	if(len(s)<2):
		return 0
	elif(s[:2]=="11"):
		return 1+count11(s[2:])
	else:
		return count11(s[1:])
print count11(s)