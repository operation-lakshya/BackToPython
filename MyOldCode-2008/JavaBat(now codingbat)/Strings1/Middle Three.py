s=raw_input("\nEnter a string of odd length(minimum length is 3):\t")
if (len(s)<3):
	print "\nSory, you have to enter a string of minimu length 3"

elif (len(s)%2==0):
	print "\nIt is an even length string so not possible to take 3 middle ones"

else:
	print s[len(s)/2-1]+s[len(s)/2]+s[len(s)/2+1]
	
raw_input("\nPress enter to finish")