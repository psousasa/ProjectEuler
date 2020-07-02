"""

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

"""

n = 600851475143
i = 2
while i * i < n:

    n, i = (n / i, i + 1) if n % i == 0 else (n, i + 1)


print(n)