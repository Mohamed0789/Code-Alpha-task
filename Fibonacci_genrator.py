"""
Fibonacci series is a sequence where each number is the sum of the two preceding numbers
we here a function to do this , give this function a number and then print out n_th fibonacci series
assume we need to print the first 9 numbers on fibonacci series
"""


def feb_nth(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    a = 0
    b = 1
    n -= 2 # subtract 2 test cases above
    while n > 0:
        c = a + b
        a = b
        b = c
        n -= 1
    return c


for i in range(1, 10):
    print(feb_nth(i))
