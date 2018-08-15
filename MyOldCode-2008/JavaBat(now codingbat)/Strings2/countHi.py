#**************************************************************************
#    Description: This Python script and this is to count hi's
#***************************************************************************

#Take a name from user 
s=raw_input("\nEnter a string to count 'hi's\t")
i=0
count=0

#loop to count hi's
while(i<(len(s)-1)):
	if(s[i:(i+2)]=="hi"):
		count=count+1
	i=i+1

#output to the user
print "\nThe total number of hi's are: ",count

#prompt user to finish
raw_input("\npress enter to finish")
