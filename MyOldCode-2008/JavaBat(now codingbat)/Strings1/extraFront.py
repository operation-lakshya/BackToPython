a=raw_input("\nEnter a string\t")
if (len(a)<2):
	print "\nOutput is: "+a+a+a
else:
	print "\nOutput is: "+a[:2]+a[:2]+a[:2]

raw_input("\nPress enter to finish")