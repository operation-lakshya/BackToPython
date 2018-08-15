
s=raw_input("\nEnter a string\t")

n=int(raw_input("\nEnter 'n input':\t"))
if (n>len(s)):
	print "\n'n input' is grater than the string length"
else:
	print s[:n]+s[(len(s)-n):]

raw_input("\nPress enter to finish")