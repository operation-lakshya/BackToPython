from array import array
a=array('i')
n=input("\nEnter the length of the array")
if(n<0):
	print "\nWrong input"
else:
	for i in range(0,n):
		a.append(input("\nenter the element"))
	if((a[0]==1 and a[1]==3) or (a[1]==1 and a[2]==3)):
		print "\nTrue"
	elif((a[n-3]==1 and a[n-2]==3) or (a[n-2]==1 and a[n-1]==3)):
		print "\nTrue"
	else:
		print "\nFalse"
raw_input("")
