# Example of generator expression

y = (n for n in range(2,10,2))

for i in range(15):
    print(next(y))

""" 
Output:
2
4
6
8
Traceback (most recent call last):
  File "generator_2.py", line 6, in <module>
    print(next(y))
StopIteration 

"""