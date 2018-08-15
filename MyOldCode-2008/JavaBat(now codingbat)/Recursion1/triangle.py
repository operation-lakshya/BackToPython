n=input("\nEnter the number of rows")
def triangle(n):
	if(n<0):
		print "\nSory! Wrong input(negative values not allowed)"
	elif(n==0):
		return 0
	else:
		return n+triangle(n-1)
print "\nThe number of blocks are: ",triangle(n)

	