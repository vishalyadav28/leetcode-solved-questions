n=len(matrix)
for i in range(n):
    for j in range(i):
        matrix[i][j],matrix[j][i] = matrix[j][i], matrix[i][j]

for i in matrix:
    i = i.reverse()
return matrix
