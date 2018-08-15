s=raw_input("\nEnter a string\t")
n=int(raw_input("\nEnter a integer between 0 to string length(inclusive):\t"))
while(n>len(s) or n<0):
	print "\nyou are given out of length integer"
	print "\nSo try again"
	print "\n************************************"
	n=int(raw_input("\nEnter a integer between 0 to string length(inclusive):\t"))
	
def repeatEnd(s,n):
	r=""
	i=1
	while(i<=n):
		j=len(s)-n
		while(j<len(s)):
			r=r+s[j]
			j=j+1
		i=i+1
	print r	
repeatEnd(s,n)
raw_input("\nPress enter to finish")