# All comparisions operations in Python have the same priority

print(False is False)   # Output: True
print(True is False)    # Output: False

print(False is False is False)
'''
Output: True
(False is False is False) is equal to: (False is False) and (False is False),
which is equal to: True and True
'''

print(2 < 18 == 22)
'''
Output: False
(2 < 18 == 22) is equal to: (2 < 18) and (18 == 22),
which is equal to: True nad False
'''