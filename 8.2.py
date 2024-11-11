def num(array):
    if len(array) > 1:
        array[0], array[-1] = array[-1], array[0]
m = int(input("Введите длину массива: "))
A = []
for i in range(m):
    element = int(input(f"Введите элемент {i + 1}: "))
    A.append(element)
print("Исходный массив:", A)
num(A)
print("Массив после замены первого и последнего элементов:", A)
