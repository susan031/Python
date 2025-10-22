import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.isqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

lower = int(input("Введи нижнюю границу диапазона: "))
upper = int(input("Введи верхнюю границу диапазона: "))

primes = []
for num in range(lower, upper + 1):
    if is_prime(num):
        primes.append(num)

print(f"Простые числа в диапазоне от {lower} до {upper}:")
print(primes)
input("")