def procInput(n, row):
    temp = [0 for i in range(n+1)]
    for i in range(n+1):
        temp[i] = int(row[i])
    return temp
    
people = procInput(int(input()), str(input()))
friends = 0
for i in range(len(people)):
    if i > sum(people[:i]) + friends:
        friends = i - sum(people[:i])
print(friends)