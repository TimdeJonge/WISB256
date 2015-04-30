import sys
import time
import math

# sys.argv is a list with the command-line arguments. sysv.arg[0] is the name of Python script
intervalTop = int(sys.argv[1])
target = str(sys.argv[2])
T1 = time.perf_counter()
primes = [2]
for i in range(3, intervalTop, 2):
    isPrime = True
    for j in primes:
        if j>math.sqrt(i):
            break
        if i%j == 0:
            isPrime = False
            break
    if (isPrime):
        primes.append(i)
    
T2 = time.perf_counter()
timeElapsed = T2 - T1
print('Found ' + str(len(primes)) + " Prime numbers smaller than " + str(intervalTop) + " in " + str(timeElapsed) +" seconds" )
fin = open(target, 'w')
for prime in primes:
    fin.write(str(prime) + "\n")