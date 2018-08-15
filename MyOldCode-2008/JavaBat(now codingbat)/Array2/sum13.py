#name:sum13
from array import array #array calling function
a=array('i') #array of typecode int
sum,j=0,0
n=int(raw_input("enter length of the array: "))
for i in range(n):
    a.append(input("enter value: ")) #entering elements to array a by using append function
while (j<n):   
    if j==0:
        if a[j]==13: #it checks whether the first element is 13 or not
            j=j+2       # if it is 13 j value is increased by 2
        else:
           sum+=a[j] 
           j+=1
           
    elif j>0:
        if a[j]==13 or a[j-1]==13: #it checks the element or its previous element is 13 or not
            sum=sum
            j+=1
        else:
            sum+=a[j] 
            j+=1
print sum           
            
