A = [[1, 0, -3], [2, 0, 1], [-1, -1, 0]]
B = [[-1, -2, 0], [-2, 3, 0], [0, 0, -3]]
m = len(A)
p = len(A[0])

n = len(B[0])

C = [[0 for _ in range(n)] for __ in range(m)]

for i in range(m):
        for j in range(n):
            s = 0
            for k in range(p):
                s += A[i][k] * B[k][j]
            C[i][j] = s

print("Matriz resultante:")
for row in C:
    print(row)