n=input("\nEnter the number")
def count7(n):
	if(n<0):
		print "\nSory! Wrong input(negative values not allowed)"
	elif(n==0):
		return 0
	else:
		if((n%10)==7):
			return 1+count7(n/10)
		else:
			return count7(n/10)
print count7(n)

	