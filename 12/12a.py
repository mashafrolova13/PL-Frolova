def power_factorial(x, n):
    if n == 0:
        return 1
    return x * power_factorial(x, n - 1) / n

x = int(input('Введите значение x:'))
n = int(input('Введите значение n:'))
result = power_factorial(x, n)
print(result)
