n=input("\nEnter the bumnnies number")
def bunnyEars(n):
	if(n<0):
		print "\nSory! Wrong input(negative values not allowed)"
	elif(n==0):
		return 0
	else:
		return 2+bunnyEars(n-1)
print "\nThe number of ears are: ",bunnyEars(n)

	