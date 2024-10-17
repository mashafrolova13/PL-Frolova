n0 = -1
l = 0
max_l = 0
n = int(input())
while n != 0:
    if n == n0:
        l += 1
    else:
        n0 = n
        max_l = max(max_l,l)
        l1 = 0
    n = int(input())
max_l = max(max_l, l)
print('Наибольшее количество подряд идущих чисел', max_l)
