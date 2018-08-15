#------------------------------------------------------------------------------
#    Description: This Python script and this is for Tea party
#------------------------------------------------------------------------------

tea=int(raw_input("\nEnter tea amount"))	#prompting user to give tea
candy=int(raw_input("\nEnter candy amount"))	#prompting user to give candy

#conditions according to hypothesis

if (tea<5 or candy<5):	#check whether tea and candy are less than 5 or not 
	print "\n bad!"	#printing output

elif (tea>=2*candy or candy>=2*tea):	
	print "\ngreat!"
else:
	print "\ngood!"

#prompting user to finish

raw_input("\nPress enter to finish")