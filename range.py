
# python 2.x - function(argument) -> list
'''
In Python 3.x range is a data type that represents a sequence of numbers
range(start, stop, step) 
by default: start = 0, step = 1
stop - the number not included in the sequence
'''


A = list(range(10))     # list - converts a range object to a list
print(A)                # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


B = list(range(30,0,-3))
print(B)               # Output: [30, 27, 24, 21, 18, 15, 12, 9, 6, 3]