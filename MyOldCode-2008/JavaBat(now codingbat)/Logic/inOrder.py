#------------------------------------------------------------------------------
#    Description: This Python script and this is for check given three 
#				numbers are in given order or not
#------------------------------------------------------------------------------

#take input from user

A=int(raw_input("\nEnter first number"))
B=int(raw_input("\nEnter second number"))
C=int(raw_input("\nEnter third number"))
b=raw_input("\nIf 'b' is relaxed give ** yes ** otherwise give ** no **\t")

#check whether the given input is in proper way or not

while (b!='no' and b!='yes'):
	print "\n*********You are giving wrong input. So try again************"
	b=raw_input("\nIf 'b' is relaxed give ** yes ** otherwise give ** no **\t")

#conditions according to hypothesis

if (C<=B):
	print "\nfalse"
elif (b=='yes'):
	print "\ntrue"
elif (B>A):
	print "\ntrue"
else:
	print "\nfalse"
#prompt user to finish
raw_input("\nPress enter to finish")