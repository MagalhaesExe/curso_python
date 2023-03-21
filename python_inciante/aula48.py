# string = 'ABCDE'
# lista = [123, True, 'Alex', 1.2, []]
# lista[-3] = 'Maria'
# print(lista)
# print(lista[2], type(lista[2]))

# lista = [10, 20, 30, 40]

# # lista[2] = 300
# # del lista[2]
# # print(lista)
# # print(lista[2])

# lista.append(50)
# lista.pop()
# lista.append(60)
# lista.append(70)
# ultimo_valor = lista.pop(3)
# print(lista, 'Removido,', ultimo_valor)

# lista = [10, 20, 30, 40]
# lista.append('Alex')
# nome = lista.pop()
# lista.append(1233)
# del lista[-1]
# # lista.clear()
# lista.insert(-2, 5)
# print(lista)

# lista_a = [1, 2, 3]
# lista_b = [4, 5, 6]
# lista_c = lista_a + lista_b
# lista_d = lista_a.extend(lista_b)
# print(lista_a)

lista_a = ['Alex', 'Maria', 1, True, 1.2]
lista_b = lista_a.copy()


lista_a[0] = 'Qualquer coisa'
print(lista_a)
print(lista_b)