import math

for a in range(100,350):
    for b in range(a,500):
        c = math.sqrt(a**2+b**2)
        d = math.floor(c)
        if d == c:
            print(a + b + d, a, b, d)
            if int(a + b + d) == 1000:
                print("SOLVED", a*b*d)