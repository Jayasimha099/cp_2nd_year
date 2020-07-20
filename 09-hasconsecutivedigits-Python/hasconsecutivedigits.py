# hasConsecutiveDigits(n)  [10pts]
# Write the function hasConsecutiveDigits(n) that takes a possibly negative int value n and returns True if that 
# number contains two consecutive digits that are the same, and False otherwise.

def hasconsecutivedigits(n):
	# your code goes here
	pass
	n=abs(n)
	temp = 0
	while (n>0):
		a = n%10
		if temp == a:
			return True
		n=n//10
		temp = a
	return False
	