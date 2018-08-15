s=raw_input("\nEnter a string")

def getSandwich(s):
	if(s.count("bread")<2):
		print "\n"
	else:
		start=s.index("bread")
		end=s[(start+5):].index("bread")
		print s[(start+5):(end+start+5)]
getSandwich(s)
raw_input("\nPress enter to finish")