'''
lambda keyword can be used to create small functions
argument: statement
'''

def plus_2(x):
    return lambda x: x + 2

a = plus_2(0)
print(a(8)) 
# Output: 10

numbers = [(3, 'tree'), (1, 'one'), (2, 'two')]

numbers_sorted = sorted(numbers, key=lambda x: x[1])
print(numbers_sorted)
''' 
lambda is used as a key - for every element returns second value
Output: [(1, 'one'), (3, 'tree'), (2, 'two')]
'''