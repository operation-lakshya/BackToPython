from array import array
A=array('i')
print "\nEnter the array elements"
i=1
print "\n********************************"
print "\nS.No\t\tElement"
while(i<=2):
	print "\n",i,
	print "\t\t",
	A.append(input(""))
	i=i+1	
if 2 in A or 3 in A:
	print "\nTrue"
else:
	print "\nFalse"	
raw_input("\nPress enter to finish")



