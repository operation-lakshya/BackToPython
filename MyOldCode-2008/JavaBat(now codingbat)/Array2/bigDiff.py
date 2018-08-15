from array import array
a=array('i')
for i in range(input("enter length of array: ")):
    a.append(input("enter value:" ))
m=max(a)
n=min(a)
print "m","=",m, "  ", "n","=",n
print "defference between m &n", "=",m-n        
