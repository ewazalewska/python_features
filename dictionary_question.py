'''
Dictionary is a set of key: value pairs, with the requirement that the keys are unique.
What will happen if keys are not unique?
'''

example = {'name': 'Ewa', 'name': 'Anna', 'name': 'Karolina'}
print(example)

""" 
Output: {'name': 'Karolina'}
In this dictionary, the keys are not unique, but it does not cause an error.
Python creates key-value pairs and assigns the values 'Ewa', 'Anna', 'Karolina' in to the key 'name'.
"""