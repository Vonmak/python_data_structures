'''
Sets
It is unordered and unindexed.
Unchangeable
Duplicates not allowed
'''

my_set={1,2,3,4,5}
for i in my_set:
    print(i)
    
# 1
# 2
# 3
# 4
# 5
    
print(4 in my_set)
# it will return a boolean of True or False

'''
add()
add items in set
'''
my_set.add(6)
print(my_set) #{1, 2, 3, 4, 5, 6}

'''
update()
add sets
'''
new_set={7,8,9}
my_set.update(new_set)
print(my_set) #{1, 2, 3, 4, 5, 6, 7, 8, 9}

# NB: you can add a list, dictionary, tuple to a set

'''
remove() or discard()
removes specific item.
but discard does not raise an error if item does not exist

pop()
removes the last element
sets are unordered so when you remove an element
using pop() you can't know whicch element has been removed
'''

'''
clear() and del
empties the set
'''

'''
Join two sets use union()
'''
set1= my_set.union(new_set)
print(set1) #{1, 2, 3, 4, 5, 6, 7, 8, 9}

'''
intersection_update()
this will only keep items that are present in the
both sets
'''
my_set1={1, 2, 3, 7, 8, 9, 8, 9}
my_set2={3, 7, 8}
new_set1={1, 8, 9,6,5}
my_set1.intersection_update(my_set2,new_set1)
print(my_set1) #{8}

'''
intersection()
this will only return a new set that only contains items
that are present in both sets
'''
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z) #{'apple'}