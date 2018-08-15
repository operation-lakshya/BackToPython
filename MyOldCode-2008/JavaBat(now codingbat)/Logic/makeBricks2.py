import math
small=int(raw_input("\nEnter the number of small bricks\t"))
big=int(raw_input("\nEnter the number of big bricks\t"))
x=int(raw_input("\nEnter the required size\t"))
a=x/5

if (a<=big and x-(a*5)<=small):
	print "\nTrue"
elif (math.fabs(x-big*5)<=small):
	print "\nTrue"
else:
	print "\nFalse"

raw_input("\nPress enter to finish")