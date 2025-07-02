# Рекурсивна проверка дали едно число е просто
def is_prime(n, divisor=2):
    if n < 2:
        return False
    if divisor * divisor > n:
        return True
    if n % divisor == 0:
        return False
    return is_prime(n, divisor + 1)

# Извеждане на всички прости числа в интервала [p, q]
p = int(input("Въведи p: "))
q = int(input("Въведи q: "))

print(f"Простите числа в интервала [{p}, {q}] са:")
for number in range(p, q + 1):
    if is_prime(number):
        print(number, end=" ")

print()
