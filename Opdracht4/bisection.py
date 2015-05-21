def findroot(f,a,b,epsilon):
    m = (a + b)/2
    print(m)
    if abs(a-b) < epsilon:
        return m
    if f(a)*f(m) < 0:
        return findroot(f,a,m,epsilon)
    elif f(b)*f(m) < 0:
        return findroot(f,b,m,epsilon)
    else:
        return "No roots found."
        
print(findroot(lambda x: x*x, -1, 10, .001))