'''
A ring is an area limited bt teo circles that have the same center but different radius.
In this task we consider rings whose center is at (0,0).

'''

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(inner, outer, points_x, points_y):
    # write your code in Python 3.6
    arr = []
    smallRad = inner*-1
    bigRad = outer*-1

    for a,b in zip(points_x,points_y):
        
        # rotation clockwise
        
        if a > 0 and b > 0:
            if a <= inner and b >= inner and b < outer:
                arr.append((a,b))
            
            elif a > inner and a < outer and b < inner:
                arr.append((a,b))
                
            elif a >inner and a < outer and b > inner and b<outer:
                arr.append((a,b))
                
        elif a > 0 and b < 0:
            if a < inner and b < smallRad and b > bigRad:
                arr.append((a,b))
            
            elif a > inner and a < outer and b > smallRad:
                arr.append((a,b))
                
            elif a >inner and a < outer and b < smallRad and b > bigRad:
                arr.append((a,b))
        
        elif a < 0 and b < 0:
            if a > smallRad and b < smallRad and b > bigRad:
                arr.append((a,b))
            
            elif a < smallRad and a > bigRad and b > smallRad:
                arr.append((a,b))
                
            elif a < smallRad and a > bigRad and b < smallRad and b > bigRad:
                arr.append((a,b))
        
        if a < 0 and b > 0:
            if a >= smallRad and b >= inner and b < outer:
                arr.append((a,b))
            
            elif a < smallRad and a < outer and b <= inner:
                arr.append((a,b))
                
            elif a < smallRad and a < outer and b > inner and b<outer:
                arr.append((a,b))
    
    return len(arr)

print(solution(2, 4, [4, 0, 1, -2], [-4, 4, 3, 0]))

print(solution(1, 3, [0, 1, 2, -2, 3], [0, 1, 4, 1, 0]))



# def fibonacci(num):
#   if num <= 0:
#     return []
#   if num == 1:
#     return [0]
#   fibonacci_list = [0,1]

#   for i in range(2, num):
#     f_num = fibonacci_list[i-1] + fibonacci_list[i-2]
#     fibonacci_list.append(f_num)

#   return fibonacci_list