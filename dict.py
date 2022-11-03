'''dictionary'''
phonebook = {
"bob": 7387,
"alice": 3719,
"jack": 7052,
}
# print(phonebook["alice"])

squares = {x: x * x for x in range(6)}
# print(squares)

import collections
# ordered dict
dic = collections.OrderedDict(one=1, two=2, three=3)
# print(dic)
dic['four']=4
# print(dic)

# default dict
# Return Default Values for Missing Keys
dd = collections.defaultdict(list)
# Accessing a missing key creates it and
# initializes it using the default factory,
# i.e. list() in this example:
dd["dogs"].append("Rufus")
dd["dogs"].append("Kathrin")
dd["dogs"].append("Mr Sniffles")

# print(dd["dogs"]) # ['Rufus', 'Kathrin', 'Mr Sniffles']

# chainmap
# groups multiple dictionaries into a single mapping.
dict1 = {"one": 1, "two": 2}
dict2 = {"three": 3, "four": 4}
chain = collections.ChainMap(dict1, dict2)

print(chain)
# ChainMap({'one': 1, 'two': 2}, {'three': 3, 'four': 4})

# ChainMap searches each collection in the chain
# from left to right until it finds the key (or fails):
print(chain["three"]) #3
print(chain["one"]) #1
print(chain["missing"] )
#Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# KeyError: 'missing'


# mappingProxyType
from types import MappingProxyType
writable = {"one": 1, "two": 2}
read_only = MappingProxyType(writable)

# The proxy is read-only:
print(read_only["one"]) #1
read_only["one"] = 23
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'mappingproxy' object does not support item assignment

# Updates to the original are reflected in the proxy:
writable["one"] = 42
read_only
# mappingproxy({'one': 42, 'two': 2})