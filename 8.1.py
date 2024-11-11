def num(number):
    for digit in str(number):
        if digit == '0' or number % int(digit) != 0:
            return False
    return True
p = int(input("Введите число p: "))
result = [n for n in range(1, p + 1) if num(n)]
print("Числа, делящиеся на каждую из своих цифр:", result)
