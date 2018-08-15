from array import array
a=array('i')
sum,j=0,0
n=int(raw_input("enter length of array"))
for i in range(n):
    a.append(input("enter values in array"))
while (j<n):
 
        if a[j]==6:
            if 7 in a[j:]:
                while (a[j]!=7):
                    sum=sum
                    j+=1
                j+=1
            else:
                sum=sum+a[j]
                j+=1
        else:
            sum=sum+a[j]
            j+=1
            
   
           
print sum
