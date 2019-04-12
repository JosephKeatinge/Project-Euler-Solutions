"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

def isPrime(n):
    # Check if number n is prime and return a boolean
    i = 2
    while i <= n // 2:
        if n % i == 0:
            return False
        i += 1
    return True

def findNthPrime(n):
    # Finds the nth number prime and returns it
    primeCount = 2
    currentNum = 3
    while primeCount < n:
        currentNum += 2
        if isPrime(currentNum):
            primeCount += 1
    return currentNum

print(findNthPrime(10001))
