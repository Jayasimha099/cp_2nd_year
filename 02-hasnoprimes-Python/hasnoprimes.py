# Write the function hasnoprimes(L) that takes a 2d list L of integers, 
# and returns True if L does not contain any primes, and False otherwise.

def check_prime(m):
	if m<=1:
			return False
	for i in range(2,m):
    		if m%i == 0:
    				return False
	return True
    			
def fun_hasnoprimes(l):
	for i in l:
    		for j in i:
    				if check_prime(j):
    						return False
	return True

