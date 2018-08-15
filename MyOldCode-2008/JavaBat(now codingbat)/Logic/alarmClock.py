#------------------------------------------------------------------------------
#    Description: This Python script and this is to calculate the sum
#						according to given hypothesis
#------------------------------------------------------------------------------

#following print state ments are for user to understand and give input

print "Hi I am calculating the sum\nSo give input"

#take input

a=int(raw_input("enter first number"))
b=int(raw_input("enter second number"))

s=a+b	#Sum calculation
if (s>=10 and s<=19):	#check condition given in hypothesis
	print "Sum is: 20"
else:
	print "Sum is:", s

#end of the programm

raw_input("press")