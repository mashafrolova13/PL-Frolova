arr = [0, 5, 25, 0, 6, 0]
aver = sum(arr) / len(arr)
arr = [aver if x == 0 else x for x in arr]
print("Массив после замены нулей:", arr)
