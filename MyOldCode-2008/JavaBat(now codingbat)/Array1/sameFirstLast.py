from array import array
n=int(raw_input("\nEnter the size of array:\t"))
while(n<=0):
	print "\Sory, you have to give size as 1 or more"
	n=int(raw_input("\nEnter the size of the array"))
print "\nEnter the elements here"
print "\nS.No\t\tElement"	
A=array('i')
i=1
while(i<=n):
	print "\n",i,
	A.append(int(raw_input("\t\t")))
	i=i+1
if(A[0]==A[len(A)-1]):
	print "\nTrue"
else:
	print "\nFalse"
raw_input("\nPress enter to finish")