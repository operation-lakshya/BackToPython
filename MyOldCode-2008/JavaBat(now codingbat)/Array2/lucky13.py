######### name : Lucky 13 ##########

from array import array #calling function
a=array('i') #a is array of int type
r="no"
n=int(raw_input("enter length of array"))
for i in range(n):
    a.append(input("enter elements in array"))
for i in range(n):
                   if a[i]==1 or a[i]==3: # it checks 1 or 3 are in the array
                       r="yes"
if r=="yes":
                   print "false"
else:
                   print "true"
