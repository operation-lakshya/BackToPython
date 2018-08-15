s=raw_input("\nEnter a string")

def xyzMiddle(s):

	if "xyz" not in s:
		print "\nThere is no 'xyz'"
	else:
		i=0
		f=0
		while(i<len(s)):
			if(s[i]=='x' and s[i+1]=='y' and s[i+2]=='z'):
				i=i+3
				while(i<len(s)):
					f=f-1
					i=i+1
			else:
				f=f+1
			i=i+1	
		if(abs(f)>1):
			print "\nFalse"
		else:
			print "\nTrue"
xyzMiddle(s)
raw_input("\nPress enter to finish")
	