import random


def read_input_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    return lines


def write_output_file(filename, result):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(result)


def task_9_1(matrix, k):
    diag_elem = matrix[k - 1][k - 1]
    if diag_elem == 0:
        return "Диагональный элемент равен 0, деление невозможно.\n"
    else:
        matrix[k - 1] = [x / diag_elem for x in matrix[k - 1]]
        result = "Обновленная матрица:\n"
        for row in matrix:
            result += " ".join(map(str, row)) + "\n"
        return result


def task_9_2(matrix):
    p = len(matrix)
    result = "Транспонированная матрица:\n"
    for i in range(p):
        for j in range(p):
            result += str(matrix[j][i]) + " "
        result += "\n"
    return result


def main():

    students_data = read_input_file('vvod.txt')

    all_results = ""
    i = 0

    while i < len(students_data):

        student_info = students_data[i].strip().split()
        if len(student_info) < 4:
            print(f"Ошибка: строка {students_data[i].strip()} имеет недостаточно данных.")
            i += 1
            continue

        fio = ' '.join(student_info[1:4])  # ФИО
        group = student_info[4]


        try:
            p = int(input(f"Введите порядок матрицы для {fio} (Группа {group}): "))
            matrix = []
            print("Введите матрицу построчно (через пробел):")
            for _ in range(p):
                row = list(map(float, input().split()))
                matrix.append(row)

            k = int(input(f"Введите номер строки (от 1 до {p}) для задания 9.1: "))
            if 1 <= k <= p:
                result_9_1 = task_9_1(matrix, k)
            else:
                result_9_1 = "Некорректное значение k\n"

            result_9_2 = task_9_2(matrix)

        except ValueError:
            print(f"Ошибка: Некорректный размер матрицы или введено неверное значение для {fio}.")
            i += 1
            continue

        all_results += f'Результаты для {fio} (Группа: {group}):\n'
        all_results += result_9_1
        all_results += result_9_2
        all_results += '\n'

        i += 1

    output_filename = "vivod_all_results.txt"
    write_output_file(output_filename, all_results)

    print(f'Результаты всех студентов записаны в файл: {output_filename}')


main()
