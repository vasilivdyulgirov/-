def str_rev(s, pos):
    if pos == len(s):
        return
    str_rev(s, pos + 1)
    print(s[pos], end='')

# Въвеждане на низ
s = input("Въведи низ: ")

# Извеждане в обратен ред
print("Низът в обратен ред е: ", end='')
str_rev(s, 0)
print()  # нов ред
