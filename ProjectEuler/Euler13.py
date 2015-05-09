fin = open("Euler13.txt","r")
listNum = []
for line in fin:
    listNum.append(int(line[:15]))
print(sum(listNum))