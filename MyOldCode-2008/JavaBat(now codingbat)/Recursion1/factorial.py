n=input("\nEnter a number to find factorial")
def factorial(n):
	if(n<0):
		return 0
	elif(n==0):
		return 1
	else:
		return n*factorial(n-1)

f=factorial(n)
if(f==0):
        print "\nThere is no factorial for negative values"
else:
        print "\nThe factorial of the number is: ",f
raw_input("\nPress Enter to finish")
