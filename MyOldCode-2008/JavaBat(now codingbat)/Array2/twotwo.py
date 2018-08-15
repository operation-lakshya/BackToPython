###################  Name :: Two Two  ###################

from array import array  # array calling function
a=array('i') # a is array of int type
n=int(raw_input("enter length of array"))
for i in range(n):
    a.append(input("enter elements in array"))
i=1
while (i<n):
    if a[i]==2:  # it checks whether the element is 2 or not
        if a[i-1]==2:  # it checks whether the precede element of 2 is 2 or not
            r="yes"
        else:
            r="no"
   
    i+=1
if r=="yes":
    print "true"
else:
    print "false"
