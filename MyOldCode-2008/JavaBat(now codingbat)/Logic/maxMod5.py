a=int(raw_input("\nEnter the first value\t"))
b=int(raw_input("\nEnter the second value\t"))
if (a==b):
	print "\n0 (Both are equal)"
elif (a%5==b%5):
	if (a<b):
		print "\n",a
	else:
		print "\n",b
elif (a<b):
	print "\n",b
else:
	print "\n",a

raw_input("\nPress enter to finish")