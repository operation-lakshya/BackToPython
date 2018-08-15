from array import array
a=array('i')
n=input("\nEnter the length of the array:\t")
k=0
while(k<n):
	a.append(input("\nEnter the element"))
	k=k+1
def array11(a,n):
	if(n==len(a)):
		return 0
	elif(a[n]==11):
		return 1+array11(a,n+1)
	else:
		return array11(a,n+1)
s=input("\nEnter an index to count for '11':\t")
print array11(a,s)
	