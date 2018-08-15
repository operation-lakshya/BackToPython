#------------------------------------------------------------------------------
#    Description: This Python script and this is for calculating the Date fashion
#------------------------------------------------------------------------------

#Following print state ments are for the user to understand and give input

print "\nHi I am calculating the Date Fashion"
print "\nAccording to the following rating codes"
print "\n********************************************************************************"
print "\nDate fashion\t\tresult"
print "\n0\t\t\tNo"
print "1\t\t\tmaybe"
print "2\t\t\tyes"
print "\n********************************************************************************"
print "\nSo please follow the instructions below"

#Take input from user

you=int(raw_input("\nPlease enter the stylishness of your clothes(ranges between 0 and 10):\t"))

#Checking it is proper input or not

while (you<0 or you>10):
	print "\n***************You are giveng wrong input. So try again******************"
	you=int(raw_input("\nPlease enter the stylishness of your clothes(ranges between 0 and 10):\t"))
#Take input from user

date=int(raw_input("\nPlease enter the stylishness of your date's clothes(ranges between 0 and 10):\t"))

#Checking it is proper input or not

while (date<0 or date>10):
	print "\n***************You are giveng wrong input. So try again******************"
	date=int(raw_input("\nPlease enter the stylishness of your date's clothes(ranges between 0 and 10):\t"))

#check conditions according to programm hypothesis

if (you<=2 or date<=2):
	print "\nSory, You got the result: 0(no)"
elif (you>=8 or date>=8):
	print "\nCongratulations!, You got the result: 2(yes)"
else :
	print "\nOk, You got the result: 1(may be)"
#ending the programm

raw_input("\nPress enter to finish")