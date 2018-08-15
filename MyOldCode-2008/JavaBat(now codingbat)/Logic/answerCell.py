#------------------------------------------------------------------------------
#    Description: This Python script and this is for cell phone answering
#------------------------------------------------------------------------------

#input section

b=int(raw_input("\nIf it is morning give ** 1 ** otherwise give ** 0 **\t"))

#checking the input is in proper way or not

while (b!=1 and b!=0):
	print "\n*********You are giving wrong input. So try again************"
	b=int(raw_input("\nIf it is morning give ** 1 ** otherwise give ** 0 **\t"))


c=int(raw_input("\nIf it is you mom call give ** 1 ** otherwise give ** 0 **\t"))

#checking the input is in proper way or not

while (c!=1 and c!=0):
	print "\n*********You are giving wrong input. So try again************"
	c=int(raw_input("\nIf it is you mom call give ** 1 ** otherwise give ** 0 **\t"))
d=int(raw_input("\nIf you are asleep give ** 1 ** otherwise give ** 0 **\t"))

#checking the input is in proper way or not

while (d!=1 and d!=0):
	print "\n*********You are giving wrong input. So try again************"
	d=int(raw_input("\nIf you are asleep give ** 1 ** otherwise give ** 0 **\t"))

#conditions

if (d==1):
	print "\nDon't Answer"
elif (b==1):
	if (c==1):
		print "\nAnswer It"
	else:
		print "\nDon't Answer"
else:
	print "\nAnswer It"
#prompting user to finish	
raw_input("\nPress enter to finish")