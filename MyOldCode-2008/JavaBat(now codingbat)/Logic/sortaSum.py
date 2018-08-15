#------------------------------------------------------------------------------
#    Description: This Python script and this is check alaram time
#------------------------------------------------------------------------------

#following print state ments are for user to understand and give input

print "\nHi I am saying when will the alaram ring"
print "\nRead the codes below to give input"
print "\n********************************************************************************"
print "\nDay\t\tCode"
print "\nSun\t\t0"
print "\nMon\t\t1"
print "\nTue\t\t2"
print "\nWed\t\t3"
print "\nThu\t\t4"
print "\nFri\t\t5"
print "\nSat\t\t6"
print "\n********************************************************************************"
print "\nPlease follow the instructions below and give input"

#take input

d=int(raw_input("\nPlease enter the Day code(must be from 0 to 6):\t"))
v=raw_input("If you are on vacation give ** true ** otherwise give ** false **\t")

#check input is in proper way or not

while (v!='true' and v!='false'):
	print "\n*********You are giving wrong input. So try again************"
	v=raw_input("\nIf you are on vacation give ** true ** otherwise give ** false **\t")

#check conditions according to programme hypothesis

if (d==0):
	if (v=='true'):
		print "\nNo alaram on that day it is off"
	else:
		print '''\nAlaram rings at "10:00"'''
else:
	if (v=='true'):
		print '''\nAlaram rings at "10:00"'''
	else:
		print '''\nAlaram rings at "7:00"'''

#end of the programm

raw_input("\nPress enter to finish")