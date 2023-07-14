'''
filter(function, iterable)
Construct an iterator from those elements of iterable for which function is true

map(function, iterable, *iterables)
Return an iterator that applies function to every item of iterable
'''

names = ['ewa zalewska', 21, ['the', 'end'], 'MARK TOWER', 'eLEONORE green']

only_names = list(filter(lambda x: type(x) is str, names))
print(only_names)
# Output: ['ewa zalewska', 'MARK TOWER', 'eLEONORE green']

final_names = list(map(lambda x: x.lower().title(), only_names))
print(final_names)
# Output: ['Ewa Zalewska', 'Mark Tower', 'Eleonore Green']