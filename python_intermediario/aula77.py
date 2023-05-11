pessoa = {}

chave = 'nome'

pessoa[chave] = 'Alex'
pessoa['sobrenome'] = 'Magalhães'

print(pessoa[chave])

pessoa[chave] = 'Maria'

del pessoa['sobrenome']
print(pessoa)
print(pessoa['nome'])

if pessoa.get('sobrenome') is None:
    print('não existe')
else:
    print(pessoa['sobrenome'])
# print('Isso não vai')