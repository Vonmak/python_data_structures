'''
a loop to find the prime numbers between a range of numbers
'''
print('Enter range:')
start = int(input("Enter a starting number: "))
stop= int(input("Enter a stopping number: "))

for i in range(start, stop):
    if i>1:
        for j in range(2, i):
            if (i%j) == 0:
                break
        else:
            print(i)