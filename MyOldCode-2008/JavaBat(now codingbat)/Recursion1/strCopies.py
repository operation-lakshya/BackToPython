s=raw_input("\nEnter a string")
t=raw_input("\nEnter a sub string to count in the given string")
n=input("\nEnter the number of copies")
def strCopies(s,t,n):
	if(n==0):
		print "True"
	elif(len(s)<len(t)):
		print "False"
	elif(s[:len(t)]==t):
		return strCopies(s[1:],t,n-1)
	else:
		return strCopies(s[1:],t,n)
strCopies(s,t,n)
	