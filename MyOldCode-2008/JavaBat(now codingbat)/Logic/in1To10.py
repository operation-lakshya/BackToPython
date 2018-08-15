#------------------------------------------------------------------------------
#    Description: This Python script and this is for in 1 to 10
#------------------------------------------------------------------------------

#Take input from user

n=int(raw_input("Enter a number"))  #Prompting user to enter number

b=raw_input("\nIf it is Outside mode give ** true ** otherwise give ** false **\t") #promptinguser to give outside mode 

#checking the input is in proper way or not

while (b!='true' and b!='false'):
	print "\n*********You are giving wrong input. So try again************"
	b=raw_input("\nIf it is Outside mode give ** true ** otherwise give ** false **\t")  #promptinguser to give outside mode 

#condition checking

if (n>=1 and n<=10):	#condition for n is between 1 to 10
	print "\ntrue"	#printing out put
elif (b=='true'):	#condition for b is true or false
	print "\ntrue"	#printing out put
else:			#else part
	print"\nfalse"	#printing out put
	
raw_input("\nPress enter to finish")	#prompting user to finish