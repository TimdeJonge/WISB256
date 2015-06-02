import math

class Vector(object):
    def __init__(self, amount=0, values=[]):
        self.amount = amount
        if type(values)==list and values != []:
            self.values = []
            for value in values:
                self.values.append(float(value))
        elif type(values) == float:
            self.values = [values for i in range(amount)]
        else:
            self.values = [0.0 for i in range(amount)]
    
    def __str__(self):
        answer = '' 
        for value in self.values:
            answer += (str(value)+"\n")
        return str(self.values)
        
    def lincomb(self, other, alpha, beta):
        result = []
        for i in range(self.amount):
            result.append(self.values[i]*alpha + other.values[i]*beta)
        return Vector(self.amount,result)
    
    def scalar(self, alpha):
        return self.lincomb(self,alpha,0)
        
    def inner(self, other):
        result = 0
        for i in range(self.amount):
            result += self.values[i]*other.values[i]
        return result
    
    def norm(self):
        return math.sqrt(self.inner(self))
        
    def projects(self,other):
        return self.scalar(other.inner(self)/self.inner(self))
    
    def __sub__(self, other):
        return self.lincomb(other, 1, -1)
        
u = Vector(2, [3,0])
v = Vector(2,2.0)
u1 = v.projects(u) -u 
print(v.inner(u1))