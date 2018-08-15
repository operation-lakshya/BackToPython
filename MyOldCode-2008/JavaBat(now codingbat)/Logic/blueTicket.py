A=int(raw_input("\nEnter the value containing A\t"))
B=int(raw_input("\nEnter the value containing B\t"))
C=int(raw_input("\nEnter the value containing C\t"))
if (A+B==10 or B+C==10 or C+A==10):
	print "\nThe result is: 10"
elif (A==C+10 or B==C+10):
	print "\nThe result is: 5"
else:
	print "\nThe result is: 0"

raw_input("\nPress enter to finish")