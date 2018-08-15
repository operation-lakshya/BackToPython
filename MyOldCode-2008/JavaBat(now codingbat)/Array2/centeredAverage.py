#name: centered average

from array import array
a=array('i')
sum=0
n=int(raw_input("enter length of array: ")) #enter length of array
if n>=3:
    for i in range(n):
        a.append(input("enter values: ")) #enter elements in the array
    a.remove(max(a)) #remove max element in a
    a.remove(min(a)) #remove min element in a
    for i in range(n-2): 
        sum+=a[i]  #sum remaining elements
    avg=sum/(n-2)
    print "centered average=",avg    
else:
    print "enter the value greater than 3"
