import os

lista = []

while True:
    print('Selecione uma opção')
    opcao = input('[i]nserir, [a]pagar, [l]istar: ')

    if opcao == 'i':
        os.system('clear')
        valor = input('O que você quer inserir? ')
        lista.append(valor)

    elif opcao == 'a':
        indice_str = input('Escolha o índice para apagar: ')

        try:
            indice = int(indice_str)
            del lista[indice]
        except:
            print('Não foi possível apagar esse índidce')
    
    elif opcao == 'l':
        os.system('clear')
        
        if len(lista) == 0:
            print('Nada para listar')

        for i, valor in enumerate(lista):
            print(i, valor)
    
    else:
        print('Escolha i, a ou l.')