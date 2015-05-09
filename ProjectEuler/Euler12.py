import math

fin = open("primes.txt", "r")
primes = []
for line in fin:
    primes.append(int(line[:-1]))


#pdivCheck requires a lookup table of primes called "primes", takes an integer "num" and returns an ordered list of all prime divisors of "num", along with their multiplicity.
#pdivCheck functions as long as the biggest prime factor of num is smaller than the square of the biggest number in primes.
def pdivCheck(num):
    i =0
    divisors = []
    while(primes[i]<=math.sqrt(num)):
        k=0
        while(num%primes[i]==0):
            num/=primes[i]
            k+=1
        if k!=0:
            divisors.append([primes[i],k])
        i+=1
    if num!=1:
        divisors.append([num,1])
    return divisors

#Dependencies:  pdivCheck
#Input:         int
#Output:        int             divisorcount of input        
def divCheck(num):
    tempList = pdivCheck(num)
    tempCount = 1
    for prime in tempList:
        tempCount *= prime[1]+1
    return tempCount
    
i=1
j=1
while(divCheck(j)<500):
    i+=1
    j+=i
print(j)