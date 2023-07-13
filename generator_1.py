'''
The yield expression is used when defining a generator function.
Can be used in the body of a function definition.
'''

def return_even_num():
    for n in range(2,10,2):
        yield n

x = return_even_num()           # generator object

print(x)

'''
Output:
<generator object return_even_num at 0x00000229CEAB8EB0>
'''

for i in range(15):
    print(next(x))

"""
Output:
2
4
6
8
Traceback (most recent call last):
  File "generator_1.py", line 20, in <module>
    print(next(x))
StopIteration 

"""