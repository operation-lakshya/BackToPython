import math
a=int(raw_input("\nEnter the first number\t"))
b=int(raw_input("\nEnter the second number\t"))
c=int(raw_input("\nEnter the third number\t"))
if (math.fabs(a-b)>=10 or math.fabs(b-c)>=10 or math.fabs(c-a)>=10):
	print "\nTrue"
else:
	print "\nFalse"
raw_input("\nPress enter to finish")
