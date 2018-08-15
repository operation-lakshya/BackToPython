base=raw_input("\nEnter the base string")
rem=raw_input("\nEnter the  remove string")
def remove(base,rem):
	if (len(base)<len(rem)):
		return base
	if(base[:len(rem)]==rem):
		return remove(base[len(rem):],rem)
	else:
		return base[0]+remove(base[1:],rem)
print remove(base,rem)		


