def check_fermat(a,b,c,n):
    try:
        a**n + b**n - c**n
    except:
        return "Those are not valid parameters!"
    if n<3:
        return "That isn't good enough!"
    
    if a**n+b**n-c**n == 0:
        return "Holy smokes, Fermat was wrong!"
    else: 
        return "Nah bruh"
        
a = input("What is the desired value for a? ")
b = input("What is the desired value for b? ")
c = input("What is the desired value for c? ")
n = input("What is the desired value for n? ")
print(check_fermat(a,b,c,n))