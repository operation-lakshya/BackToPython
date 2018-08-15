from array import array
A=array('i')
a=input("\nEnter the size of the array(1 or more)")
while(a<=0):
	print "\nSory, you have given an empty array"
	a=input("\nEnter the size of the array(1 or more)") 

print "\nEnter the array elements"
i=1
print "\n********************************"
print "\nS.No\t\tElement"
while(i<=a):
	print "\n",i,
	print "\t\t",
	A.append(input(""))
	i=i+1

if(a==1):
	B=array('i',[A[0],A[0]])
	print "\nThe result array is: ",B.tolist()
else:
	B=array('i',[A[0],A[a-1]])
	print "\nThe result array is: ",B.tolist()
	
raw_input("")




