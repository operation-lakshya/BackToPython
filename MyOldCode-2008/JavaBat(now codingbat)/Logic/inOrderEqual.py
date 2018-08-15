#------------------------------------------------------------------------------
#    Description: This Python script and this is for check whether 
#				they are in strict increasing order
#------------------------------------------------------------------------------

#input from user

A=int(raw_input("\nEnter first number"))
B=int(raw_input("\nEnter second number"))
C=int(raw_input("\nEnter third number"))
b=raw_input("\nif equality is relaxed give ** yes ** otherwise give ** no **\t")

#checking the input is in proper way or not

while (b!='yes' and b!='no'):
	print "\n*********You are giving wrong input. So try again************"
	b=raw_input("\nf equality is relaxed  give ** yes ** otherwise give ** no **\t")

#conditions according to hypothesis

if (B>A and C>B): 

	if ((C-B)%(B-A)==0):
		print "\ntrue"
elif (b=='yes'):
	if (B==A or C==B):
		print "\ntrue"
	else:
		print "\nfalse"

else:
	print "\nfalse"
#prompting user to finish
raw_input("\nPress enter to finish")
