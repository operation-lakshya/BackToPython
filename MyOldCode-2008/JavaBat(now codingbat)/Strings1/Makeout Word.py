
#********************************************************************
#    Description: This Python script and this is for Make out word programm 
#********************************************************************
#input: take out input and word input from user
s=raw_input("\nEnter the Out Input(must be even length):\t")
t=raw_input("\nEnter the word input:\t")
#Print the word in outinputs
print s[0:len(s)/2]+t+s[len(s)/2:len(s)]
#Prompt user to finish
raw_input("\nPress enter to finish")







