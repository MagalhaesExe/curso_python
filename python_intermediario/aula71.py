x, y, *resto = 1, 2, 3, 4
print(x, y, resto)

# def soma(x, y):
#     return x + y

def soma(*args):
    total = 0
    for numero in args:
        total += numero
    return total

soma_1_2_3 = soma(1, 2, 3)

soma_4_5_6 = soma(4, 5, 6)

numeros = 7, 8, 9, 98, 324, 0, 3
soma_7_8_9 = soma(*numeros)

# print(sum((7, 8, 9, 98, 324, 0, 3)))
print(*numeros)