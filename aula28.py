nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')
nome_invertido = nome[::-1]

if nome and idade:
    print('Seu nome é', nome)
    print('Seu nome invertido é', nome_invertido)

    if ' ' in nome:
        print('Seu nome contém espaços')
    else:
        print('Seu nome não contém espaços')

    print('Seu nome tem', len(nome), 'letras')
    print('A primeira letra do seu nome é', nome[0])
    print('A última letra do seu nome é', nome[-1])
else:
    print('Desculpa, você deixou campos vazios')
