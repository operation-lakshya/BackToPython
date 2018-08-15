from array import array
a=array('i')
n=input("\nEnter the length of the array")
if(n<3 or n%2==0):
	print "\nWrong input"
else:
	for i in range(0,n):
		a.append(input("\nenter the element"))
	b=array('i')
	q=int(n/2)
	b.append(a[q-1])
	b.append(a[q])
	b.append(a[q+1])
	print b.tolist()

raw_input("")
