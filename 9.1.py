p = int(input("Введите порядок матрицы (p): "))
matrix = []
print("Введите матрицу построчно (через пробел):")
for _ in range(p):
    row = list(map(float, input().split()))
    matrix.append(row)
k = int(input(f"Введите номер строки (от 1 до {p}): "))
if 1 <= k <= p:
    diag_elem = matrix[k-1][k-1]  
    if diag_elem == 0:
        print("Диагональный элемент равен 0, деление невозможно.")
    else:
        matrix[k-1] = [x / diag_elem for x in matrix[k-1]]
        print("Обновленная матрица:")
        for row in matrix:
            print(" ".join(map(str, row)))
else:
    print("Некорректное значение k")
