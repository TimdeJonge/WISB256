import random
import math


def drop_needle(L):
    needleX = random.random()
    angle = random.vonmisesvariate(0,0)
    needleX2 = needleX + L* math.cos(angle)
    
    if needleX2 > 1 or needleX2 < 0:
        #print(needleX, angle, needleX2)
        return True
    else:
        return False
length = 0.9
count = 0
tries = 10**7
for i in range(tries):
    if(drop_needle(length)):
        count += 1
        
print("count =", count)
print("pi =", (2*tries*length)/count)