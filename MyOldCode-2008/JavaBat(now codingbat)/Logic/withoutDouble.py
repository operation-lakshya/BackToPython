a=int(raw_input("\nEnter the first dice value\t"))
b=int(raw_input("\nEnter the second dice value\t"))
c=raw_input("\nIf the no Doubles is true give **true** otherwise give **false**\t")
h=1
if (c!='true' and c!='false'):
	print "\nyou are not given (true/false) properly"
	h=0

if (c=='true' and a==b):
	if (a==6 and b==6):
		sum=7
		print "\nThe sum is :",sum
	else:
		print "\nThe sum is :",a+b+1
elif(h==1):
	print "\nThe sum is :",a+b

raw_input("\nPress enter to finish")
