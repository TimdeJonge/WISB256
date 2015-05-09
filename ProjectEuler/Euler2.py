sumValues = 0
tempList = [1,1]
i = 0
def fibonacci(n):
    
    try:
        return tempList[n]
    except:
        tempList.append(fibonacci(n-1) + fibonacci(n-2))
        return (tempList[n])

while(fibonacci(i) < 4*10**6):
    if fibonacci(i)%2 == 0:
        sumValues += fibonacci(i)
    i+=1

print sumValues