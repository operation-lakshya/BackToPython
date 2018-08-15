s=raw_input("\nEnter a string")
n=int(raw_input("\nEnter an integer between 1 to lengthof the string"))
while(n>len(s) or n<1):
	print "\nyou are given out of length integer"
	print "\nSo try again"
	print "\n************************************"
	n=int(raw_input("\nEnter a integer between 1 to string length:\t"))
	

def prefixAgain(s,n):
	if s[:n] in s[n:]:
		print "\nTrue"
	else:
		print "\nFalse"
prefixAgain(s,n)
raw_input("\nPress enter to finish")