
#********************************************************************
#    Description: This Python script and this is for Extra End 
#********************************************************************
#input: Take a string from user
s=raw_input("\nEnter a string(length should be minimum 2):\t")
if (len(s)==1):
	print "\nSory, you have to enter a string of length 2"
#Print the last rwo letters of 3 copies
else:
	print s[-2:]+s[-2:]+s[-2:]
#Prompt user to finish
raw_input("\nPress enter to finish")






