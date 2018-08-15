#**************************************************************************
#    Description: This Python script and this is to check equality of 
#					cats and dogs in the given string
#***************************************************************************

#Take a name from user 
s=raw_input("\nEnter a string\t")
cat=0
dog=0
i=0

#loop to check count of cat's and dog's
while(i<len(s)-2):
	if(s[i:(i+3)]=="cat"):
		cat=cat+1
	if(s[i:(i+3)]=="dog"):
		dog=dog+1
	i=i+1

#checking of equality of cat's and dog's
if(cat==dog):
	print "\nTrue"
else:
	print "\nFalse"

#prompt user to finish
raw_input("\nPress enter to finish")