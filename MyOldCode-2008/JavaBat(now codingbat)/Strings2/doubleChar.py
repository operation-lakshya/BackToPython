#**************************************************************************
#    Description: This Python script and this is for print double characters
#***************************************************************************

#Take a name from user 
s=raw_input("\nEnter a string to print the double characters")
i=0
t=""

#loop to print double characters
while (i<len(s)):
	t=t+s[i]+s[i]
	i=i+1
#output to the user
print t

#prompt user to finish
raw_input("\nPress enter to finish")











s=raw_input("\nEnter a person name to say hello to that person:\t")
#Print the given name with hello
print "\nHello",s
#Prompt user to finish
raw_input("\nPress enter to finish")