from array import array
n=input("\nEnter the size of the array")
a=array('i')
i=1
print "\nS.No\t\tElement"
while(i<=n):
	print "\n",i,
	print "\t\t",
	a.append(input(""))
	i=i+1
a.reverse()
i=0
print "\nThe array in reverse order: ",
print "{",
while(i<len(a)):
	print a[i],
	if(i!=len(a)-1):
		print ",",
	i=i+1
print "}"
raw_input("\nPress enter to finish")	
