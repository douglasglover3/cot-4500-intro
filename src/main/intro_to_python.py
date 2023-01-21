import numpy as np

matrix1 = np.zeros((3,3))
for i in range(3):
    matrix1[i][i] = 1

matrix2 = np.copy(matrix1)
for i in range(3):
    for j in range (3):
        if matrix2[i][j] == 0:
            matrix2[i][j] += 3

matrix3 = np.delete(matrix2, 2, 1)

print(matrix1)
print(matrix2)
print(matrix3)