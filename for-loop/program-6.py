
# 6.  Write a PYTHON program to compute the cosine series
#           cos(x) = + (x0 / 0!) – (x2 / 2!) + (x4 / 4!) – (x6 / 6!) + … xn / n!

import math

n = int(input("Enter a number: "))
n = math.radians(n)
terms = 50

def fact(num):
    f = 1
    for i in range(1, num+1):
        f = f * i
    return f

cos_sum = 0
sign = 1

for i in range(0, 2 * terms, 2):
    term = (n ** i) / fact(i)
    cos_sum += sign * term
    sign *= -1  

print(round(cos_sum, 4))