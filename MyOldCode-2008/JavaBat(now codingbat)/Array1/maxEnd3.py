from array import array
a=array('i')
i=1
print "\nS.No\t\tElement"
while(i<=3):
	print "\n",i,
	print "\t\t",
	a.append(input(""))
	i=i+1
if(a[0]>a[2]):
	a[1],a[2]=a[0],a[0]
else:
	a[0],a[1]=a[2],a[2]

print a
raw_input("\nPress enter to finish")
	