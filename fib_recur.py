'''A Fibonacci sequence is the integer sequence of 0, 1, 1, 2, 3, 5, 8....
The first two terms are 0 and 1. All other terms are obtained by adding
the preceding two terms.This means to say the nth term is the sum of (n-1)th and (n-2)th term.'''

#RECURSIVE
"""Recursive function to
   print Fibonacci sequence"""
def fib_recur(n):
    """ assumes n an int >= 0 """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_recur(n-1) + fib_recur(n-2)

# Change this value for a different result
num_of_terms = int(input("How many terms do want in the sequence: "))
# check if the number of terms is valid
if num_of_terms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence: ")
   for i in range(num_of_terms):
       print(fib_recur(i))

#ITERATIVE
'''
def fib(n):
# the assignment to 'a & b' is of order O(1):constant
    a,b = 1,1
#the "for loop" is of order O(n): linear
    for i in range(n-1):
        a,b = b,a+b
#the "return statement" is of order O(1):constant
    return a
print(fib(10))
'''
#Therefore The Worst case for fibonacci_iterative = O(1) + O(n) + O(1) = O(n).
#In the Recursive method,the recursion breaks down in the order 2^n
#The Worst Case = O(2n)
#Therefore the performance of the Iterative method is more efficient than the Recursive method.
