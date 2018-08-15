a=raw_input("\nEnter a string\t")
b=raw_input("\nEnter the ord\t")
if (len(b)==1):
	print "\nOutput is: "+a[0]
elif (b[1:]==a[1:len(b)]):
	print "\nOutput is: "+a[:len(b)]
else:
	print "seshu"


raw_input("\nPress enter to finish")