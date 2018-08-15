from array import array
A=array('i')
n=int(raw_input("\nEnter the size of the array"))
if(n<0):
	print "\nWrong input"
else:
	for i in range(0,n):
		A.append(input("\nEnter the element"))
	i=1
	while(i<n):
		store = A[i]
		j=i-1
		while(j>=0 and A[j]>store):
			A[j+1] = A[j]
			j=j-1
		A[j+1]=store
		i=i+1
	element=input("\nEnter the element to search")
	found=-1
	last=n
	mid=1
	first=0
	while(mid>0 and mid<n-1):
		mid=int((first+last)/2)
		if(A[mid]==element):
			found=mid
			break
		elif(A[mid]<element):
			first=mid
		else:
			last=mid
	if(found==-1):
		print "\nThe element is not found"
	else:
		print "\nThe element is found at index ",found
raw_input("\nPress enter to finish")