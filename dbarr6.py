def rec(i, k):
    if i == k:
        print(i, end=" ")
        return
    print(i, end=" ")   # Прав ход на рекурсията (преди)
    rec(i + 1, k)       # Рекурсивно извикване
    print(i, end=" ")   # Обратен ход на рекурсията (след)
n = int(input("Въведи n: "))
rec(1, n)
print()  # За нов ред след отпечатване
