from array import array
import math
pi=math.pi
a=array('i')
i=1
while(i<=3):
	a.append(int(pi))	
	pi=(pi*10)%10
	i=i+1
print str(a)
raw_input("\nPress enter to finish")

