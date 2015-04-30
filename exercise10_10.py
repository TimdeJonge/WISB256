fin = open('words.txt') 
testList = []
for line in fin:
    testList.append(line[:-1])
fin.close()

for word in testList:
    if word[1::2] in testList and word[::2] in testList:
        print(word[::2], word[1::2])
        