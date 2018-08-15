a=raw_input("\nEnter a string\t")
if (len(a)<2):
	print a
else:
	t=a[:len(a)-2]
	t=t+a[len(a)-1]+a[len(a)-2]
	print t

raw_input("\nPress enter to finish")