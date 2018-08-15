from array import array  #array calling function
a=array('i')  # a is an array of int type code
n=int(raw_input("enter length of the array"))
for i in range(n):
    a.append(input("enter values"))
count,i=0,0
while (i<n):
    if i<n-2:
        if  a[i]==3: # it checks whether the array contains 3 or not
           if a[i+1]==3: # it checks whether there is a next to 3 or not
                break
           else:
                count+=1
    
    elif i==n-1:
        if a[n-1]==3  and a[n-2]!=3: # it checks whether the last element is 3 but not it's previous one
            count+=1
    i+=1
if count==3:
    print "true"
else:
    print "false"
