from array import array
a=array('i')
for i in range(0,3):
	a.append(input("\nenter the element"))
for i in range(0,2):
	if(a[i]==2 and a[i+1]==3):
		a[i+1]=0
print a.tolist()
	
raw_input("")
