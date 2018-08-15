#------------------------------------------------------------------------------
#    Description: This Python script and this is for check Last Digit 
#					according to given hypothesis
#------------------------------------------------------------------------------
#input from user
A=int(raw_input("\nEnter first number"))
B=int(raw_input("\nEnter second number"))
C=int(raw_input("\nEnter third number"))
#assign ments for get unit place digits
a=A%10
b=B%10
c=C%10.
#check conditions the unit digits equality

if (a==b or b==c or c==a):
	print "\ntrue"
else:
	print "\nfalse"

#propmt user to finish
raw_input("\nPress enter to finish")
