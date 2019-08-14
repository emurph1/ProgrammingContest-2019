nums = [int(i) for i in input().split()]
a = max(nums)
b = min(nums)

def primeFinder(n):
    primes = []
    for i in range(2, b):
        if n % i == 0: # testing for divisibility
            isPrime = True
            for j in range(2, i): # testing for prime
                if i % j == 0:
                    isPrime = False
                    break
            if isPrime:
                primes.append(i)
    return primes

def matches(primes_one, primes_two):
    matches = []
    for n in primes_one:
        if primes_two.__contains__(n):
            matches.append(n)
    return matches

primes_a = primeFinder(a)
primes_b = primeFinder(b)

matching_primes = matches(primes_a, primes_b)

for i in matching_primes:
    primes_a.pop(primes_a.index(i))

if (len(primes_a) + len(primes_b)) == 0:
    print("0.0")
else:
    print((len(matching_primes))/(len(primes_a) + len(primes_b)))
