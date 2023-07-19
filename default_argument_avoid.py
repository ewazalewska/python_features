'''
The default argument, in this case an empty list, 
is created ONCE during the function definition
and is reused in subsequent function calls.
'''

def add_to_list(element, list_A=[]):    
    list_A.append(element)
    return list_A

print(add_to_list(10))      # Output: [10]
print(add_to_list(5,[3,4])) # Output: [3, 4, 5]

print(add_to_list(20))      # Output: [10, 20]
