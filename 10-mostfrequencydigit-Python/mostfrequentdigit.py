# mostFrequentDigit(n) [10pts]
# Write the function mostFrequentDigit(n), that takes a non-negative integer n and returns the digit from 0 to 9 
# that occurs most frequently in it, with ties going to the smaller digit.

def mostfrequentdigit(n):
	# your code goes here
	pass
	n = abs(n)
	if n == 0:
		return 0
	
	dic = {}
	count = 0
	a = 0
	while n!=0:
		a = n%10
		if a in dic.keys():
			dic[a] += 1
		else: 
			dic[a] =1
		n=n//10

	for i in dic.keys():
		if dic[i]>count:
			count = dic[i]
			a = i
		elif dic[i] == count and i<a:
			a =i
	return a
		