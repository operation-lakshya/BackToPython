from array import array
a=array('i')
n=input("\nEnter the size")
if(n==0):
	print "\nThe sum2 is: 0"
else:	
	i=1
	print "\nS.No\t\tElement"
	while(i<=n):
		print "\n",i,
		print "\t\t",
		a.append(input(""))
		i=i+1
	if(n==1):
		print "\nThe sum2 is:",a[0]
	else:
		print "\nThe sum2 is:",a[0]+a[1]
raw_input("\nPress enter to finish")