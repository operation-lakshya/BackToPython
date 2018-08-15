from array import array
a=array('i')
n=input("Enter the size of the array")
for i in range(0,n):
	a.append(input("Enter the element"))
def bubblesort(a):
	i=1
	while(i<n):
		swap = "false"
		j=0
		while(j<n-i):
			if(a[j]>a[j+1]):
				s=a[j]
				a[j]=a[j+1]
				a[j+1]=s
				swap = "true"
			j=j+1
		if(swap=="false"):
			break
		i=i+1
def selectionsort(a):
	i=0
	while(i<n):
		min = i
		j = i+1
		while(j<n):
			if(a[j]<a[min]):
				min = j
			j=j+1
		if(a[i]>a[min]):
			s = a[i]
			a[i] = a[min]
			a[min] = s
		i=i+1
def insertion_sort(a):
	i=1
	while(i<n):
		store = a[i]
		j=i-1
		while(j>=0 and a[j]>store):
			a[j+1]=a[j]
			j=j-1
		a[j+1]=store
		i=i+1
bubblesort(a)
print "Bubble sort:"
print a
selectionsort(a)
print "Selection sort:"
print a
insertion_sort(a)
print "Insertion sort:"
print a