'''
count occurence of elements in a string 
'''

def solution(A):
    B=[int(i)for i in A]
    
    n=len(B)
    # init an empty array
    y=[]
    # init a dict
    count = dict()
    # loop through the elements of the array
    for x in range(n-1):

        if (B[x] == B[x + 1]):
            y.append(B[x])
        elif(B[x] != B[x + 1]) and (B[x] == B[x - 1]):
            y.append(B[x])
    
    print(y)
    # find the length of the elements appende to the empty array     
    k=len(y)   
    # loop through the elements of the array
    for i in range(k):
        if y[i] in count.keys():
            count[y[i]] += 1
        else:
            count[y[i]] = 1
    print(count)
    # find the max value of a key in dict count
    max_key =max(count, key=count.get)
    
    # find the value of the max key
    value=count.get(max_key)
    
    return f'{max_key}.Occurs {value}times'
            

# print(solution('1012771116'))
print(solution('5673336579999900000'))
