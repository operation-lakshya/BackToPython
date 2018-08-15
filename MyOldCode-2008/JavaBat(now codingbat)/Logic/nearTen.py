#------------------------------------------------------------------------------
#    Description: This Python script and this is for near ten
#------------------------------------------------------------------------------
#input section

n=int(raw_input("\nEnter a number"))	#prompt user to enter number

#conditions acording to hypothisis

if (n<8):		
	print "\nfalse"
elif (10-n%10<=2):
	print "\ntrue"
else:
	print "\nfalse"
#prompting user to finish

raw_input("\nPress enter to finish")