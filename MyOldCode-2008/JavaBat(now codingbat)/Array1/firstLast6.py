from array import array
n=int(raw_input("\nEnter the size of the array(1 or more)"))
while(n<=0):
	print "\Sory, you have to give size as 1 or more"
	n=int(raw_input("\nEnter the size of the array"))
print "\nEnter the elements here"
print "\nS.No\t\tElement"
A=array('i')
i=1
while(i<=n):
	print "\n",i,
	print "\t\t",
	A.append(int(raw_input("")))
	i=i+1
if(A[0]==6 or A[-1]==6):
	print "\nTrue"
else:
	print "\nFalse"
raw_input("\nPress enter to finish")