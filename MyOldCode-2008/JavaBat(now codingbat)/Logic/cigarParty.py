#------------------------------------------------------------------------------
#    Description: This is Python script and this is for check the party 
#						success full or not
#------------------------------------------------------------------------------

#following print state ments are for user to understand and give input

print "\nHi I am said that.. is the party successfull or not?"
print "\nSo please follow the instructions below"

#take input

c=int(raw_input("\nPlease enter the number of cigars\t"))
b=int(raw_input("\nEnter the week day(it should be like 1 for monday.....7 for saturday\t"))

#checking the input is in proper way or not

while (b<1 or b>7):
	print "\n*********You are giving wrong input. So try again************"
	b=int(raw_input("\nEnter the week day(it should be like 1 for monday.....7 for saturday\t"))

#check conditions according to programm hypothesis

if (c>=40):
	if (c<=60):
		print "\nResult is TRUE\nCongratulations!, Your party is successfull"
	elif (b==6 or b==7): 
		print "\nResult is TRUE\nCongratulations!, Your party is successfull"
	
	else:
		print "\nResult is FALSE\nSory, Your party is not successfull"	
else:
	print "\nResult is FALSE\nSory, Your party is not successfull"

#prompt user to finish
raw_input("\nPress enter to finish")