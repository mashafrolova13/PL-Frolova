p = int(input("Введите порядок матрицы (p): "))
matrix = [list(map(int, input().split())) for _ in range(p)]
for i in range(p):
    for j in range(p):
        print(matrix[j][i], end=" ")
    print()
