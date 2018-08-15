from array import array
a=array('i')
n=input("\nEnter the length of the array")
for i in range(0,n):
	a.append(input("\nenter the element"))
if(n==0 or n==1):
	print a.tolist()
else:
	print "{",a[0],",",a[1],"}"

raw_input("")
