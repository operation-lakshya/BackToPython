from array import array #array calling function
nums1=array('i') 
nums2=array('i')
count=0
n=int(raw_input("enter length of array"))
for i in  range(n):
    nums1.append(input("enter values in array  nums1"))
    nums2.append(input("enter values in array nums2"))

    if nums1[i]>nums2[i]:
        if nums1[i]-nums2[i]<=2 and  nums1[i]-nums2[i]!=0 : #it checks the difference between 
            count+=1                                                                            #arrays is 2 or less than 2         
                                                                                              
    else:
        if nums2[i]-nums1[i]<=2 and nums2[i]-nums1[i]!=0 : ##it checks the difference between 
            count+=1                                                                            #arrays is 2 or less than 2         
           
           
   
print count        
    
