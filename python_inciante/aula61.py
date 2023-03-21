# #      012345678
# cpf = '86915173013'
# nove_digitos = cpf[:9]
# contagem = 10
# soma = 0
# resultado = 0
# for digito in nove_digitos:
#     soma += int(digito) * contagem
#     contagem -= 1

# print(soma)
# mult = soma * 10
# print(mult)
# resto = mult % 11
# print(resto)

# if resto > 9:
#     resultado = 0
# else:
#     resultado = resto

# print(f'O primeiro digito do CPF é {resultado}')

cpf = '86915173013'
nove_digitos = cpf[:9]
contador_regressivo_1 = 10

resultado_digito_1 = 0
for digito_1 in nove_digitos:
    resultado_digito_1 += int(digito_1) * contador_regressivo_1
    contador_regressivo_1 -= 1
digito_1 = (resultado_digito_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0
print(digito_1)