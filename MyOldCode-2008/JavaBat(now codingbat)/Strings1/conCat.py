a=raw_input("\nEnter a string\t")
b=raw_input("\nEnter a string\t")
if (len(b)==0 or len(a)==0):
	print "\nOutput is: "+a+b
elif (a[len(a)-1]==b[0]):
	print "\nOutput is: "+a+b[1:]
else:
	print "\nOutput is: "+a+b


raw_input("\nPress enter to finish")