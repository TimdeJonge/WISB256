#DEFINITIONS
grid = [[] for i in range(20)]
vectors = [[1,1], [0,1], [1,0], [1,-1]]
i = 0
maximum = 0
fin = open("Euler11.txt","r")
for line in fin:
    grid[i] = line.split(" ")

    i+=1
    grid[i-1][-1] = grid[i-1][-1][:-1]

grid[19][19] +="8" #Ugly single case fix, but it makes work a lot easier.

for vector in vectors:                                                                              #allowing for future extension to more dimensions
    for i in range(max(0, -3*vector[0]), min(len(grid), len(grid) - 3*vector[0])):                  #iterating so that we won't go out of bounds. min and max such that the maximum value reached will stay in [0, len(grid)]
        for j in range(max(0, -3*vector[1]), min(len(grid), len(grid) - 3*vector[1])):
            product =1
            for k in range(4):
                product*=int(grid[i+k*vector[0]][j+k*vector[1]])
            if product > maximum:
                maximum = product
                print(product, i, j, vector)
                    