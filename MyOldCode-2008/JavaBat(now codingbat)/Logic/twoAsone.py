#------------------------------------------------------------------------------
#    Description: This Python script and this is for Two as One Given three intss
#------------------------------------------------------------------------------
#take input from user
a=int(raw_input("\nEnter first number"))
b=int(raw_input("\nEnter second number"))
c=int(raw_input("\nEnter third number"))

#conditions according to hypothesis

if (a+b==c or b+c==a or c+a==b):
	print "\nIt is possible"
else:
	print "\nNot possible"

#prompting user to finish

raw_input("\nPress enter to finish")
