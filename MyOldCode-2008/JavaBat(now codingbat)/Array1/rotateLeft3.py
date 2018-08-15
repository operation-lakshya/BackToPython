from array import array
a=array('i')
i=1
print "\nS.No\t\tElement"
while(i<=3):
	print "\n",i,
	print "\t\t",
	a.append(input(""))
	i=i+1
a.append(a.pop(0))
i=0
print "{",
while(i<len(a)):
	print a[i],
	if(i!=len(a)-1):
		print ",",
	i=i+1
print "}"


raw_input("\nPress enter to finish")	