import random
import math
import sys



def drop_needle(L):
    needleX = random.random()
    angle = random.vonmisesvariate(0,0)
    needleX2 = needleX + L* math.cos(angle)
    
    if needleX2 > 1 or needleX2 < 0:
        #print(needleX, angle, needleX2)
        return True
    else:
        return False
#definitions
try:
    tries = int(sys.argv[1])
    length = float(sys.argv[2])
except:
    print("Use: estimate_pi.py N L")
    quit()

try:
    random.seed(sys.argv[3])
except:
    pass

count = 0
smallLength = True

if(length > 1):
    smallLength = False


#main loop
for i in range(tries):
    if(drop_needle(length)):
        count += 1
        
#output
print(count, "hits in", tries, "tries")
if smallLength:
    print("Pi =", (2*tries*length)/count)
else:
    #x = math.sqrt(length**2-1)+math.asin(length**-1)
    #print(x)
    #print(length - x)
    #print(count/tries - 1)
    #print((length - x) / (count/tries - 1))
    print("Pi =", 2*(length - (math.sqrt(length**2 - 1)+math.asin(1/length)))/(count/tries - 1))