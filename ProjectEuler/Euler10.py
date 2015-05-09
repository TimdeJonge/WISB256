import math
primes = [2]

i=3
while(i < 2*10**6):
    isPrime = True
    for j in primes:
        if j>math.sqrt(i):
            break
        if i%j == 0:
            isPrime = False
            break
    if (isPrime):
        primes.append(i)
    i+=2
print(sum(primes))