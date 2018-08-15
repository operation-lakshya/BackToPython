from array import array
a=array('i')
n=input("\nEnter the length of the array:\t")
k=0
while(k<n):
	a.append(input("\nEnter the element"))
	k=k+1
def array6(a,n):
	if(n==len(a)):
		print "False"
	elif(a[n]==6):
		print "True"
	else:
		array6(a,n+1)
s=input("\nEnter an index to check for '6':\t")
array6(a,s)
	