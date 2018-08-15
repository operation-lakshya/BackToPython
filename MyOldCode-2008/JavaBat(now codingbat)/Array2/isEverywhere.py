####### name : Is Every where ########

from array import array #array calling function
a=array('i') #a is array of int type
n=int(raw_input("enter length of the array"))
v=int(raw_input("enter value to be repeated"))
count,i=0,0
if n%2!=0: #it checks n is even or odd
    print "pairing of all the elements is not possible\n so enter even length"
else:
    while(i<n):
        a.append(input("enter values"))
        
        if i%2!=0:  #it checks index value is even or odd
            if a[i]==v or a[i-1]==v: #it checks v is there in each pair or not
               count+=1
               
            else:
               break
        i+=1
if count==(n/2): #it checks whether are n/2 no.of  v's or not
    print "true"
else:
    print "false"
            
    
    
