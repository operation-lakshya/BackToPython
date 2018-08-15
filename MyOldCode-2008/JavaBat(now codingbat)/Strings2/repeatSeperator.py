s=raw_input("\nEnter a string\t")
w=raw_input("\nEnter a word\t")
n=int(raw_input("\nEnter a integer between 0 to string length(inclusive):\t"))
while(n>len(s) or n<0):
	print "\nyou are given out of length integer"
	print "\nSo try again"
	print "\n************************************"
	n=int(raw_input("\nEnter a integer between 0 to string length(inclusive):\t"))

def repeatSeparator(s,w,n):
	i=0
	res = ""
	while(i<n):
		res+=s
		if(i<(n-1)):
			res+=w
		i=i+1
	print res
repeatSeparator(s,w,n)
raw_input("\nPress enter to finish")	