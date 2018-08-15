A=int(raw_input("\nEnter the value containing A\t"))
B=int(raw_input("\nEnter the value containing B\t"))
C=int(raw_input("\nEnter the value containing C\t"))
if (A==B==C==2):
	print "\nThe result is: 10"
elif (A==B==C):
	print "\nThe result is: 5"
elif (A!=B and A!=C):
	print "\nThe result is: 1"
else:
	print "\nThe result is: 0"

raw_input("\nPress enter to finish")