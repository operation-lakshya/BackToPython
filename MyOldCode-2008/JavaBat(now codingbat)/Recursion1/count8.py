n=input("\nEnter the number")
def count8(n):
	if(n<0):
		print "\nSory! Wrong input(negative values not allowed)"
	elif(n==0):
		return 0
	elif((n%10)==8):
		if((n/10)%10==8):
			return 1+(2*count8(n/10))
		else:
			return 1+count8(n/10)
	else:
		return count8(n/10)			
print "\nThe count is: ",count8(n)
	
		