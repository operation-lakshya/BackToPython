from array import array
a=array('i')
n=input("\nEnter the length of the array")
if(n<1 or n%2==0):
	print "\nWrong input"
else:
	for i in range(0,n):
		a.append(input("\nenter the element"))
	b=array('i')
	q=int(n/2)
	if(a[0]>a[q] and a[0]>a[n-1]):
		print a[0]
	elif(a[q]>a[0] and a[q]>a[n-1]):
		print a[q]
	else:
		print a[n-1]
raw_input("")
