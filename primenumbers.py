# To take input from the user
num = int(input("Enter a number: "))

# prime numbers are greater than 1
if num >1:
    # check for factors34
    for i in range(2,num):
        if (num % i) == 0:
            print(num, 'is not a primenumber.')
            print(i,"times",num//i,"is",num)
            break
    
    else:
        print(num, 'is a primenumber.')
    
# if input number is less than
# or equal to 1, it is not prime

else:
        print(num, 'is not a primenumber.')