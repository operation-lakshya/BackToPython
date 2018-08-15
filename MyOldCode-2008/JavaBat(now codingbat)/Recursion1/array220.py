from array import array
a=array('i')
n=input("\nEnter the length of the array:\t")
k=0
while(k<n):
	a.append(input("\nEnter the element"))
	k=k+1
def array220(a,n):
	if(n==len(a)-1):
		print "False"
	elif(a[n+1]==2*a[n]):
		print "True"
	else:
		array220(a,n+1)
s=input("\nEnter an index to check for '6':\t")
array220(a,s)
	