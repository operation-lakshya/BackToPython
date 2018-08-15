from array import *
A=array('i')
n=input("\nEnter the length of the array(1 or more)")
while(n<=0):
	print "\nSory! wrong input try again"
	n=input("\nEnter the length of the array(1 or more)")

print "\nEnter the array elements"
i=1
print "\n********************************"
print "\nS.No\t\tElement"

while(i<=n):
	print "\n",i,
	print "\t\t",
	A.append(input(""))
	i=i+1

b=array('i',[0]*(2*n))
b[-1]=A[-1]
print "\nTher result array is: ",b.tolist()
print b

raw_input("\nPress enter to finish")




