# dicetoorderedhand(a, b, c) [5pts]
# Write the function dicetoorderedhand(a, b, c) that takes 3 dice and
# returns them in a hand, which is a 3-digit integer. However, even if the
# dice are unordered, the resulting hand must be ordered so that the largest
# die is on the left and smallest die is on the right. For example:
# assert(dicetoorderedhand(1,2,3) == 321)
# assert(dicetoorderedhand(6,5,4) == 654)
# assert(dicetoorderedhand(1,4,2) == 421)
# assert(dicetoorderedhand(6,5,6) == 665)
# assert(dicetoorderedhand(2,2,2) == 222)
# Hint: You can use max(a,b,c) to fsind the largest of 3 values, and
# min(a,b,c) to find the smallest.

def dicetoorderedhand(a, b, c):
	# your code goes here
	pass
	l = max(a,b,c)
	m = min(a,b,c)
	if(a<l and a>m) or a==(c or l or m or b):
    		return l*100 + a*10 +m
	
	if b<l and b>m:
    		return l*100 + b*10 + m
	
	if c<l and c>m:
    		return l*100+ c*10 +m
	