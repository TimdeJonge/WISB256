import math
maximum = 0

def isPalindrome(n):
    if len(n)<2:
        return True
        
    if n[0] == n[-1]:
        newArg = n[1:-1]
        return isPalindrome(newArg)
    else:
        return False

for i in range(800,1000):
   for j in range(800,1000):
       if isPalindrome(str(i*j)):
           if i*j > maximum:
             maximum = i*j
                
print(maximum)