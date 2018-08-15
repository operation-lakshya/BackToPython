#------------------------------------------------------------------------------
#    Description: This Python script and this is for near ten
#------------------------------------------------------------------------------
#input section

a=int(raw_input("\nEnter first number"))	#prompt user to enter a number

b=int(raw_input("\nEnter second number"))	#prompt user to enter a number

#conditions

if (a>=13 and a<=19): 	#check whether a is between 13 and 19
	print "\nTeen sum is 19"	#printing output

elif (b>=13 and b<=19):		#check whether b is between 13 and 19	
	print "\nTeen sum is 19"	#printing output
else:					#else part
	print "\nTeen sum is",a+b	#printing out put

#prompting user to finish
	
raw_input("\nPress enter to finish")