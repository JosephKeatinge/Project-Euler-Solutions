"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

def isPrime(n):
    # Check if number n is prime and return a boolean
    i = 2
    while i <= n // 2:
        if n % i == 0:
            return False
        i += 1
    return True

def largestPrimeFactor(number):
    # Find and return the largest prime number that's a factor of number
    fLow = 2
    while fLow <= number // 2:
        if number % fLow == 0:
            fHigh = number // fLow
            if isPrime(fHigh):
                return fHigh
        fLow += 1

print(largestPrimeFactor(600851475143)) 