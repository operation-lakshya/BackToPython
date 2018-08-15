######## name : Either 24 ########

from array import array #array calling function
a=array('i') #a is array of int type
n=int(raw_input("enter length of array"))
count,value=0,0
for i in range(n):
    a.append(input("enter value in array"))
for i in range(n-1):
    if a[i]==2 and a[i+1]==2: #it checks whether the  2's are in side by side or not
        count=1
    elif a[i]==4 and a[i+1]==4: #it checks whether the 4's are in side by side or not
        value=1
if count==value: # it checks whether there are both 2 & 4's in the array
    print "false"
else:
    print "true"
