# Write the function bonusFindIntRoots(a,b,c) that takes 
# the int coefficients a, b, c of a quadratic equation of this form:
#      y = ax2 + bx + c
# You are guaranteed the function has 2 real roots, and in fact that 
# the roots are all integers. Your function should return these 2 int roots 
# in increasing order. How does a function return multiple values? Like so:
# return root1, root2

import math
def fun_find_int_roots(a, b, c):
	determinant = (b*b)-(4*a*c)
	sqroot = math.sqrt(determinant)
	x1 = (-b+sqroot) / (2*a)
	x2 = (-b-sqroot) / (2*a)
	return x1, x2


