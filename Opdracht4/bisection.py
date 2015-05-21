import math

def findroot(f,a,b,epsilon):
    a = float(a)
    b = float(b)
    m = (a + b)/2
    if abs(a-b) < epsilon:
        return m
    if f(a)*f(m) <= 0:
        return findroot(f,a,m,epsilon)
    elif f(b)*f(m) <= 0:
        return findroot(f,b,m,epsilon)
    else:
        return "No roots found."

def findAllRoots(f,a,b,epsilon):
    h = abs(a-b)/epsilon
    solutions = []
    for i in range(int(math.floor(h)/2)):
        answer = findroot(f,a+2*i*epsilon, a+(i+1)*2*epsilon,epsilon)
        if answer != "No roots found.":
            print answer
            solutions.append(answer)
    for i in solutions:
        for j in solutions:
            if i!=j:
                if abs(i - j) < epsilon:
                    print(i,j)
                    solutions.remove(i)
    return solutions
    
print(findAllRoots(lambda x: (x-1)*(x-2)*(x-3), 0, 100, .01))