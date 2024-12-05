import math

def X(x1, x2):
    x1=abs(x1)
    x2=abs(x2)
    return x2/x1
d=1000000

for i in range(3):
    x1=int(input())
    x2=int(input())
    

    d=min(X(x1, x2), d)
    if d == X(x1, x2):
        x=x1
        y=x2
print(d)

################################################################

def sito_of_eratosthenes(limit):
    is_prime = [True] * (limit + 1)
    p = 2
    while (p * p <= limit):
        if (is_prime[p] == True):
            for i in range(p * 2, limit + 1, p):
                is_prime[i] = False
        p += 1
    return [p for p in range(2, limit + 1) if is_prime[p]]
def find_palindromic_primes(n):
    palindromic_primes = []
    primes = sito_of_eratosthenes(n) 
    for prime in primes:
        binary_representation = bin(prime)[2:] 
        if binary_representation == binary_representation[::-1]:
            palindromic_primes.append(prime)
    return palindromic_primes
n =int(input())
result = find_palindromic_primes(n)
print(f"Простые числа <= {n}, двоичная запись которых является палиндромом: {result}")
