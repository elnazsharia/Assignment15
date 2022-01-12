def createMatrix(n):
    matrix = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            row.append(1)
        matrix.append(row)
        i, j = 0, 0
    for i in range(n):

        for j in range(i):
            if i > 0 and j > 0:
                matrix[i][j] = matrix[i - 1][j] + matrix[i-1][j-1]
    return matrix


n = int(input())
print(createMatrix(n))
