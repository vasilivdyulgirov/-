def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x - 1)

# Въвеждане
n = int(input("n = "))
result = factorial(n)

# Извеждане
print(f"{n}! = {result}")
