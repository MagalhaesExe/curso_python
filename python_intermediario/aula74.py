def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar

falar_bom_dia = criar_saudacao('Bom dia')
falar_boa_noite = criar_saudacao('Bom tarde')

print(falar_bom_dia('Alex'))
print(falar_boa_noite('Ana'))

for nome in ['Maria', 'Luiz', 'José']:
    print(falar_bom_dia(nome))
    print(falar_boa_noite(nome))

