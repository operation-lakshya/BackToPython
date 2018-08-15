a=int(raw_input("\nEnter the number between 10-99\t"))
b=int(raw_input("\nEnter the number between 10-99\t"))
q=a%10
if (q==b%10 or q==(b/10)%10):
	print "\nTrue"
else:	
	a=a/10
	q=a%10
	if (q==b%10 or q==(b/10)%10):
		print "\nTrue"
	else:
		print "\nFalse"




raw_input("\nPress enter to finish")