# Create a Python function that checks if a number is a prime number. in range from and to
# the prime numbers is the number that can be divisible by 1 and itself and > 1
num = 2
for i in range(2, 20):
    for j in range(2, i):
        if i % j == 0:
            # print(i, 'No, it is Not prime no.')
            break
    else:
            print(i, 'Yes, it is prime no')

