'''
list: Mutable Dynamic Arrays
This means a list allows elements to be added or removed, 
and the list will automatically adjust the backing store 
that holds these elements by allocating or releasing memory.
'''
arr = ["one", "two", "three"]
print(arr)
arr[1]= 'hello'
print(arr)
del arr[1]
print(arr)
# Lists can hold arbitrary data types:
arr.append(23)
print(arr)



my_list = [1,2,3,4,2,2,3,3,4,]
names = ["Xander", "Buffy", "Angel", "Willow", "Giles"]

'''
Index()
Finds the index value of value passed
where it has been encountered the 1St Time.
'''
print(my_list.index(2)) 
# 1

'''
Count()
Finds the count of the value passed to it.
'''
print(my_list.count(2))
# 3

'''
Sorted() & Sort()
used to sort values of the list sorted has a 
return type while the sort modifies the original list
'''
print(sorted(my_list))
# [1, 2, 2, 2, 3, 3, 3, 4, 4]
my_list.sort(reverse=True)
print(my_list)
# [4, 4, 3, 3, 3, 2, 2, 2, 1]
names.sort()
print(names)
# ['Angel', 'Buffy', 'Giles', 'Willow', 'Xander']

'''
Len()
Returns the lenth of the list
'''
print(len(my_list))
# 9