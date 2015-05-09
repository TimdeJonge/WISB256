def ggd(a,b):
    if b ==0:
        return a
    elif a>b:
        return ggd(b, a%b)
    else:
        return ggd(b,a)

def kgv(a,b):
    return a*b/ggd(a,b)
temp = 1
for i in range(2,21):
    temp = kgv(temp, i)