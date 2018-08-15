a=int(raw_input("\nEnter the value containing A\t"))
b=int(raw_input("\nEnter the value containing B\t"))
c=int(raw_input("\nEnter the value containing C\t"))
if (a==b==c):
	print "\nThe sum is: 0"
elif (a==b):
	print "\nThe sum is:",c
elif (b==c):
	print "\nThe sum is:",a
elif (a==c):
	print "\nThe sum is:",b
else:
	print "\nThe sum is:",a+b+c

raw_input("\nPress enter to finish")