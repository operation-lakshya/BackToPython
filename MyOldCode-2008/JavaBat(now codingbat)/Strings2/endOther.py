import string
s=raw_input("\nEnter a string\t")
t=raw_input("\nEnter a string\t")
if(len(s)<len(t)):
	if s.lower() in t[(len(t)-len(s)):].lower():
		print "\nTrue"
elif t.lower() in s[(len(s)-len(t)):].lower():
		print "\nTrue"
else:
	print "\nFalse"

raw_input("\nPress enter to finish")