# Correct way to use an empty list as an argument

def add_to_list(element, list_B=None):
    if list_B is None:
        list_B = []
    list_B.append(element)
    return list_B

print(add_to_list(10))      # Output: [10]
print(add_to_list(5,[3,4])) # Output: [3, 4, 5]
print(add_to_list(20))      # Output: [20]