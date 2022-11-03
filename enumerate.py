x=['eat', 'sleep', 'repeat']
y='victor'

print(list(enumerate(x)))
print(list(enumerate(y)))

# printing the tuples in object directly
for ele in enumerate(x):
    print (ele)
    
# getting desired output from tuple
for count, ele in enumerate(x):
    print(count)
    print(ele)
    
color = [k for (i,k) in enumerate(x) if i not in (0,2)]
print(color)
'''
Output:

[(0, 'eat'), (1, 'sleep'), (2, 'repeat')]

[(0, 'v'), (1, 'i'), (2, 'c'), (3, 't'), (4, 'o'), (5, 'r')]

(0, 'eat')
(1, 'sleep')
(2, 'repeat')

0
eat
1
sleep
2
repeat

['sleep']
'''