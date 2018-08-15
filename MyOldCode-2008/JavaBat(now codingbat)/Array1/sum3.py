from array import array
a=array('i')
i=1
print "\nS.No\t\tElement"
while(i<=3):
	print "\n",i,
	print "\t\t",
	a.append(input(""))
	i=i+1
print "\nThe sum of elements in the array is:",sum(a)
raw_input("\nPress enter to finish")	