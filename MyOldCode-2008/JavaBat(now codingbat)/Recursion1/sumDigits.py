n=input("\nEnter a number")
sum=0
def sumDigits(n):
	global sum
	if(n<0):
		print "\nSory! Wrong input(negative values not allowed)"
	elif(n==0):
		return 0
	else:
		return (n%10)+sumDigits(n/10)
print "\nThe sum of digits in the given number is: ",sumDigits(n)

	