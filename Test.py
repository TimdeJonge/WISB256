import sys
import math

target = str(sys.argv[1])
primes = [2]
twinCount = 0
twinConstant = 0.6601618
for i in range(3, target, 2):
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

lastPrime = primes[-1]
print("Largest Prime = " +str(lastPrime)) 
print("--------------------------------")
print("pi(N)         = " + str(len(primes))) 
print("N\log(N)      = " + str(lastPrime/math.log(lastPrime)))
print("ratio         = " + str(len(primes) / (lastPrime/math.log(lastPrime))))
print("--------------------------------")
print("pi_2(N)       = " + str(twinCount))
print("2CN/log(N)^2  = " + str(lastPrime *2*twinConstant/(math.log(lastPrime)**2)))
print("ratio         = " + str(twinCount / (lastPrime *2*twinConstant/(math.log(lastPrime)**2))))
