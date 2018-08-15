#------------------------------------------------------------------------------
#    Description: This Python script and this is to calculate 
#						caught speeding
#------------------------------------------------------------------------------

#following print state ments are for user to understand and give input

print "\nHi I am calculating the caught speeding"
print "\n*********************************************************************"
print "\nHere are the codes"
print "\nCode\t\tTicket"
print "\n0\t\tNo"
print "1\t\tSmall"
print "2\t\tBig" 
print "\n*********************************************************************"
print "\nSo please follow the instructions given below" 

#take input

speed=int(raw_input("\nPlease enter your speed"))
b=raw_input("\nIf today is your birthday give ** true ** otherwise give ** false **")

#check input is in proper way or not

while (b!='true' and b!='false'):
	
	print "\n*********You are giving wrong input. So try again************"
	b=raw_input("\nIf it is the weekend give ** true ** otherwise give ** false **\t")

#check conditions according to programme hypothesis

if (b=='true'):
	if (speed<=65):
		print "\nThe result is: 0\nSo enjoy you got no ticket"
	if (speed>65 and speed<=85):
		print "\nThe result is: 1\nSo you got small ticket"
	if (speed>85):
		print "\nThe result is: 2\nSo you got big ticket"
else:
	if (speed<=60):
		print "\nThe result is: 0\nSo enjoy you got no ticket"
	if (speed>60 and speed<=80):
		print "\nThe result is: 1\nSo you got small ticket"
	if (speed>80):
		print "\nThe result is: 2\nSo you got big ticket"

#end of the programme

raw_input("\nPress enter to finish")