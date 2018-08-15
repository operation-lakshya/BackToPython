#------------------------------------------------------------------------------
#    Description: This Python script and this is for check the party 
#						success full or not
#------------------------------------------------------------------------------

#following print state ments are for user to understand and give input

print "\nHi I am said that... is squirrels play or not?"
print "\nSo please follow the instructions below"

#take input

c=int(raw_input("\nPlease enter the temperature\t"))
b=int(raw_input("\nIf it is summer give '1' otherwise give '0'\t"))

#check input is in proper way or not.

while (b!=0 and b!=1):
	print "\n*********You are giving wrong input. So try again************"
	b=int(raw_input("\nIf it is summer give '1' otherwise give '0'\t"))

#checking conditions according to programme hypothesis

if (c>=60):
	if (c<=90):
		print "\nThe result is TRUE\nsquirrels are playing in that day"	
	elif (c<=100 and b==1): 
		print "\nThe result is TRUE\nsquirrels are playing in that day"
	
	else:
		print "\nThe result is FALSE\nSory, squirrels not playing in that day"	
else:
	print "\nThe result is FALSE\nSory, squirrels not playing in that day"

#ending of the programm

raw_input("\nPress enter to finish")