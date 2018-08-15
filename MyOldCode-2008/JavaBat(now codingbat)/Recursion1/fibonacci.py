n=input("\nEnter the number to print fibonacci series")
def fibonacci(n):
	a,b=0,1
	if(n<0):
		print "\nNo Fibonacci series"
	elif(n==0):
		return a
	elif(n==1):
		return b
	else:
		return fibonacci(n-2)+fibonacci(n-1)
print "\nThe Fibonacci Series of the given number is: ",
k=0
while(k<=n):
	print fibonacci(k),
	k=k+1
print "\nThe",n,"th Fibonacci number is: ",fibonacci(n)
raw_input("\n")
		
	 