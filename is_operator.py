'''
This example shows difference between '==' and 'is' operator
value comparison: ==
identity comparison: is
'''

var1 = 'python'

var2 = var1 + '!'
var2 = var2[:-1]

print(var1, id(var1))       # Variables have different id but the same value
print(var2, id(var2))

print("Is value the same? ", var1 == var2)          # Output: True
print("Are the variables the same? ", var1 is var2) # Output: False