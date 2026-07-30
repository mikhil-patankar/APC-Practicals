# Write a PYTHON program to check the entered number is prime or not

n = int(input("Enter a number: "))

if n <= 1:
    print(f"{n} is not a prime number.")
else:
    is_prime = True
    i = 2
    while i <= n // 2:
        if n % i == 0:
            is_prime = False
            break
        i += 1

    if is_prime:
        print(f"{n} is a prime number.")
    else:
        print(f"{n} is not a prime number.")
