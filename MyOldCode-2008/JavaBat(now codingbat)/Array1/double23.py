from array import array
n=input("\nEnter the array size(0-2 inclusive):\t")
while(n>2):
	print "\nSory, wrong input size. Try again"
	n=input("\nEnter the array size(0-2 inclusive):\t")
if(n==0):
	print "\nFalse"
else:
	a=array('i')
	i=1
	print "\nS.No\t\tElement"
	while(i<=n):
		print "\n",i,
		print "\t\t",
		a.append(input(""))
		i=i+1
	if(a.count(2)==2 or a.count(3)==2):
		print "\nTrue"
	else:
		print "\nFalse"
raw_input("\nPress enter to finish")
