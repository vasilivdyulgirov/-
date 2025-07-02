def BinCode(x):
    if x != 0:
        BinCode(x // 2)
        print(x % 2, end='')

# Въвеждане
n = int(input("n = "))
print("Binary code is: ", end='')
if n == 0:
    print(0)
else:
    BinCode(n)
print()  # за нов ред
