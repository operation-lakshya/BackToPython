a=raw_input("\nEnter a string\t")
b=raw_input("\nEnter a string\t")
if (len(a)<len(b)):
	print "\nOutput is: "+a+b[len(b)-len(a):]
elif (len(a)>len(b)):
	print "\nOutput is: "+a[len(a)-len(b):]+b
else:
	print "\nOutput is: "+a+b



raw_input("\nPress enter to finish")