'''
Write a function:

def solution(A):
such that, given an array A consisting of N integers, it returns the maximum among all one-digit integers.

For example, given array A as follows:

[-6, -91, 1011, -100, 84, -22, 0, 1, 473]
the function should return 1.

Assume that:

N is an integer within the range [1...1,000]
Each element of array A is an integer within the range [-10,000..10,000].
There is at least one element in array A which satisfies the condition in the task statement

'''

def solution(A):
    try:
        return max(i for i in A if -9<=i<=9)
    except ValueError:
        return ValueError('Could not find a single digit in the list')
    
print(solution([-6, -91, 1011, -100, 84, -22, 8, 1, 473]))


# def solutionB(A):
#     max(A,key=lambda num: -10001 if num > 9 else num)

def solutionC(A):
    return max([i for i in A if len(str(i))==1])
print(solutionC([-6, -91, 1011, -100, 84, -22, 8, 1, 473]))


def solution(A):
    # write your code in Python 3.6
    arr=[]
    for i in A:
        if -9 <= i <=9:
            arr.append(i)
    return max(arr)
# a=[]
# print('Enter Array:',a)
# print(
#     max(
#         [-6, -91, 1011, -100, 84, -22, 0, 1, 473],
#         key=lambda num: -9 if num > 9 else num
#     )
# )