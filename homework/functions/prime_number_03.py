# Create a Python function that checks if a number is a prime number.
# the prime numbers is the number that can be divisible by 1 and itself and > 1
def is_num_prime(num):
    if num <= 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True


#main program
if is_num_prime(1):
    print('Yes, it is prime no.')
else:
    print('No, it is not prime no.')
