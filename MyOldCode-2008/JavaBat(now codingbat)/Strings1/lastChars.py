a=raw_input("\nEnter a string\t")
b=raw_input("\nEnter a string\t")
if (len(a)==0 and len(b)==0):
	print "\nOut put is: @@"
elif (len(a)==0):
	print "\nOutput is: @"+b[len(b)-1]
elif (len(b)==0):
	print "\nOutput is: "+a[0]+"@"
else:
	print "\nOutput is: "+a[0]+b[len(b)-1]	


raw_input("\nPress enter to finish")