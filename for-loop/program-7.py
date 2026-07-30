# 7.  Write a short PYTHON program to check weather the 
#      square root of number is prime or  not.

n = int(input("Enter a number: "))

sqr = n ** 0.5

def isPrime(num):
    for i in range(2, int(num/2)):
        if num % i == 0:
            return False
    return True

print(f"Square root of {n} is prime: {isPrime(sqr)}")