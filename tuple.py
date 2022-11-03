'''
tuple: Immutable Containers
This means elements can't be added or removed dynamically
all elements in a tuple must be defined at creation time.
To change elements in a tuple you have to convert them to
List  and alter them.
'''
arr = ("one", "two", "three")
print(arr)
'''
arr[1] = "hello" #TypeError: 'tuple' object does not support item assignment
del arr[1] #TypeError: 'tuple' object doesn't support item deletion

Tuples can hold arbitrary data types:
(Adding elements creates a copy of the tuple)
'''
print(arr + (23,))


my_tuples =(1,2,4,5,6,7)
print(my_tuples)

'''
Add Tuple to Tuple
'''
tuple2=('5',)
my_tuples+=tuple2
print(my_tuples)
# (1, 2, 4, 5, 6, 7, '5')

# can't delete items
# TypeError: 'tuple' object doesn't support item deletion
# del my_tuple[3]

del my_tuples
# NameError: name 'my_tuple' is not defined
print(my_tuples)