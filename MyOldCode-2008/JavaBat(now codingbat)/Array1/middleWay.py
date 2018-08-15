from array import array

def ainput(array):
	i=1
	print "\nS.No\t\tElement"
	while(i<=3):
		print "\n",i,
		print "\t\t",
		array.append(input(""))
		i=i+1	


A=array('i')
B=array('i')		

print "\nEnter the first array elements"
ainput(A)

print "\nEnter the second array elements"
ainput(B)

C=array('i',[A[1],B[1]])
print "Result array is: ",C.tolist()
raw_input("\nPress enter to finish")
