import random

x,y = eval(input("Enter X and Y: "))
points = [[1, 1], [2, 1], [2, 2], [3, 2], [2, 3], [3, 3], [3, 4], [1, 5], [2, 5]]

grid = []
for i in range(1,x+1):
    for j in range (1,y+1):
        temp = [i, j]
        grid.append(temp)
print(grid)

group = []
for i in points:
    for j in points:
        if i[0] == j[0] - 1 and i[1] == j[1]:
            if i not in group:
                group.append(i)
            if j not in group:
                group.append(j)
        if i[0] == j[0] + 1 and i[1] == j[1]:
            if i not in group:
                group.append(i)
            if j not in group:
                group.append(j)
        if i[1] == j[1] - 1 and i[0] == j[0]:
            if i not in group:
                group.append(i)
            if j not in group:
                group.append(j)
        if i[1] == j[1] + 1 and i[0] == j[0]:
            if i not in group:
                group.append(i)
            if j not in group:
                group.append(j)

print(group)
print(len(group))