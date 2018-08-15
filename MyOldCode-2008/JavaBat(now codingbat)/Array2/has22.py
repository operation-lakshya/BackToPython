#### Name: Has 22 #####

from array import array #array calling function
a=array('i') #array of int typecode         
r="no"
n=int(raw_input("enter length of the array:")) #enter length of array
for i in range(n):
    a.append(input("enter elements in array")) #enter elements in array, using append function
for i in range(n-1):
    if a[i]==2:            #1.
        if a[i+1]==2:   # 2. steps 1&2 checks 2 is immediately followed by 2 or not
            r="yes"
            break          # if r="yes" the loop will terminate
if r=="yes":
    print "true"
else:
    print "false"
