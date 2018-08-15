###### Name : Has 12 #######

from array import array  #array calling function
a=array('i') # a is array of int type
n=int(raw_input("enter length of array"))
for i in range(n):
    a.append(input("enter values in array"))
if 1 in a:  # it checks whether 1 is in a or  not
 
    for i in range(n):
        if a[i]==1:       # it checks whether the element in array is 1 or not
            result="false"
        elif a[i]==2:    # it checks whether the element in array is 2 or not
            result="true"
    print result
else:
    print "false"
