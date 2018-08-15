A=raw_input("\nEnter a string")
if (len(A)<2):
	if (len(A)==0):
		print "\nOutput is: @@"
	else:
		print "\nOutput is: "+A+"@"
else:
	print "\nOutput is: ",A[:2]
raw_input("\nPress enter to finish")