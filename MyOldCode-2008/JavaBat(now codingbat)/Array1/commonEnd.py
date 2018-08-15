from array import array
a=input("\nEnter the size of the first array") 
b=input("\nEnter the size of the second array")
A=array('i')
B=array('i')
def ainput(size,array):
	i=1
	print "\nS.No\t\tElement"
	while(i<=size):
		print "\n",i,
		print "\t\t",
		array.append(input(""))
		i=i+1	
		
print "\nEnter the first array elements"
ainput(a,A)
print "\nEnter the second array elements"
ainput(b,B)

if(A[0]==B[0] or A[a-1]==B[b-1]):
	print "\nTrue"
else:
	print "\nFalse"

