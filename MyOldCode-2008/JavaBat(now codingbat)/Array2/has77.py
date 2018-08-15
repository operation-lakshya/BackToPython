from array import array  #array calling function
a=array('i') # a is array of int type
n=int(raw_input("enter length of array"))
for i in range(n):
    a.append(input("enter elements in array"))
r="no"
i=0
if 7 in a:  #it checks whether 7 is in a or not
    if a.count(7)>=2:
        for i in range(n):
            r="no"
            if ((a[i]==7 and i+1<n and a[i+1]==7) or (a[i]==7 and i+2<n and a[i+2]==7)):
                r="yes"
    else:
        print "there are no two 7's"
else: 
    print "wrong input\n enter the data with 7,s"
if r=="yes":
    print "out put is true"
else:
    print "so the out put is false"

