"""Implement a function recursively to get the desired
Fibonacci sequence value.
Your code should have the same input/output as the 
iterative code in the instructions."""

def fib(n):
    if n<=1:
        return n
    return fib(n-1)+fib(n-2)

def get_fib(position):    
    return fib(position)