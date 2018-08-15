base=input("\nEnter the base value")
n=input("\nEnter the power value")
def powerN(base,n):
	if(base<1 or n<1):
		print "\nSory both values must be 1 or more"
	elif(n==1):
		return base
	else:
		return base*powerN(base,n-1)
print "\n",base,"to the power of",n,"is: ",powerN(base,n)
		