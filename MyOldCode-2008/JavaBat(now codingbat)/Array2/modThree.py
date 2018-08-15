######### Name :: Mod Three ############

from array import array #array calling function
a=array('i') # a is array of int type
n=int(raw_input("enter length of array"))
r="no"
for i in range(n):
    a.append(input("enter elements in array"))
for i in range(n-2):
    if a[i]%2==0 and a[i+1]%2==0 and a[i+2]%2==0: #it checks whether the three successive 
        r="yes"                                                                       # elements are even or not
    elif a[i]%2!=0 and a[i+1]%2!=0 and a[i+2]%2!=0: # it checks whether the three successive
           r="yes"                                                                   #  elements  are odd or not
if r=="yes":
    print "true"
else:
    print "false"
