s=raw_input("\nEnter a string\t")
n=int(raw_input("\nEnter a integer\t"))

while(n>len(s) or n<0):
	print "\nyou are given out of length integer\t"
	print "\nSo try again"
	print "\n************************************"
	n=int(raw_input("\nEnter a integer between 0 to string length(inclusive):\t"))

def repeatFront(s,n):
	r=""
	i=n
	while(i>=1):
		j=0
		while(j<i):
			r=r+s[j]
			j=j+1
		i=i-1
	print r
repeatFront(s,n)
raw_input("\nPress enter to finish")