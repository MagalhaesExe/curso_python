nome = 'Alex'
# print(nome[0])
# print(nome[1])
# print(nome[2])
# print(nome[3])

# print('x' in nome)
# print('Al' in nome)
# print(10 * '-')
# print('x' not in nome)
# print('aL' not in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')
