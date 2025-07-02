# Рекурсивна функция за сума по четни индекси
def sum_even_indexes(arr, index=0):
    if index >= len(arr):
        return 0
    return arr[index] + sum_even_indexes(arr, index + 2)

# Въвеждане на масив
n = int(input("Въведи брой елементи: "))
arr = []
for i in range(n):
    value = int(input(f"arr[{i}] = "))
    arr.append(value)

# Извеждане на сумата по четни индекси
result = sum_even_indexes(arr)
print(f"Сумата на елементите с четни индекси е: {result}")
