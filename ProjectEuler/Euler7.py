import math
primes = [2]
twinCount = 0
twinConstant = 0.6601618

i=3
while(len(primes)<10002):
    isPrime = True
    for j in primes:
        if j>math.sqrt(i):
            break
        if i%j == 0:
            isPrime = False
            break
    if (isPrime):
        if i == primes[-1] + 2:
            twinCount+=1
        primes.append(i)
    i+=2
print(primes[10000])